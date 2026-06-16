$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:8080/")
$listener.Start()
Write-Output "Listening on http://localhost:8080/ ..."

$baseDir = "E:\Bachelor\sem VI\MINORPROJECT\slide template\-latex-presentation-beamer-template-tcioe-main"

try {
    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        $urlPath = $request.RawUrl
        # Remove query parameters
        if ($urlPath.Contains("?")) {
            $urlPath = $urlPath.Substring(0, $urlPath.IndexOf("?"))
        }

        # Map to local file path
        if ($urlPath -eq "/" -or $urlPath -eq "/extractor.html") {
            $filePath = Join-Path $baseDir "extractor.html"
        } else {
            $filePath = Join-Path $baseDir $urlPath.TrimStart('/')
        }

        if (Test-Path $filePath -PathType Leaf) {
            $bytes = [System.IO.File]::ReadAllBytes($filePath)
            
            # Content type mapping
            $ext = [System.IO.Path]::GetExtension($filePath)
            $contentType = "application/octet-stream"
            if ($ext -eq ".html") { $contentType = "text/html" }
            elseif ($ext -eq ".js") { $contentType = "application/javascript" }
            elseif ($ext -eq ".pdf") { $contentType = "application/pdf" }
            elseif ($ext -eq ".txt") { $contentType = "text/plain" }

            $response.ContentType = $contentType
            $response.ContentLength64 = $bytes.Length
            $response.OutputStream.Write($bytes, 0, $bytes.Length)
        } else {
            $response.StatusCode = 404
            $errBytes = [System.Text.Encoding]::UTF8.GetBytes("File not found: $urlPath")
            $response.OutputStream.Write($errBytes, 0, $errBytes.Length)
        }
        $response.OutputStream.Close()
    }
} finally {
    $listener.Stop()
    Write-Output "Server stopped."
}
