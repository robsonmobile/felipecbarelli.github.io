import json
import os, sys
import glob
reload(sys)  
sys.setdefaultencoding("utf8")

diretorios = os.listdir("../portfolio/")

templateIndex = open("template-index.html", "r").read()
templateIndexGrid = open("template-index-grid.html", "r").read()
templateProject = open("template-project.html", "r").read()
templateProjectGrid = open("template-project-grid.html", "r").read()
finalIndexGrid = ""

with open("data.json") as arquivoJson:    
  data = json.load(arquivoJson)

name = data["name"]
about = data["about"]
github = data["github"]
curriculum = data["curriculum"]
contact = data["contact"]

for diretorio in diretorios:
  if diretorio != ".DS_Store":
    tempTemplateIndexGrid = templateIndexGrid
    tempTemplateProject = templateProject
    finalProjectGrid = ""

    with open("../portfolio/" + diretorio + "/data.json") as arquivoJson:    
      data = json.load(arquivoJson)
    tempTemplateIndexGrid = tempTemplateIndexGrid.replace("{{slug}}", diretorio, 1)
    tempTemplateIndexGrid = tempTemplateIndexGrid.replace("{{project}}", data["project"], 1)
    tempTemplateIndexGrid = tempTemplateIndexGrid.replace("{{for}}", data["for"], 1)
    tempTemplateIndexGrid = tempTemplateIndexGrid.replace("{{thumb}}", "portfolio/" + diretorio + "/thumb.jpg", 1)
    finalIndexGrid = finalIndexGrid + tempTemplateIndexGrid

    arquivosPortfolio = os.listdir("../portfolio/" + diretorio +"/")
    for arquivoPortfolio in arquivosPortfolio:
      tempTemplateProjectGrid = templateProjectGrid
      if arquivoPortfolio[-3:] == 'png' or arquivoPortfolio[-3:] == 'jpg' or arquivoPortfolio[-4:] == 'jpeg':
        if arquivoPortfolio != "thumb.jpg":
          tempTemplateProjectGrid = tempTemplateProjectGrid.replace("{{image}}", "portfolio/" + diretorio + "/" + arquivoPortfolio)
          finalProjectGrid = finalProjectGrid + tempTemplateProjectGrid;

    if len(str(data["url"])) < 10:
      url = "Unavailable"
    else:
      link = data["url"]
      url = '<a href="' + link + '" target="_blank">' + link + '</a>'

    tempTemplateProject = tempTemplateProject.replace("{{name}}", name, 1)
    tempTemplateProject = tempTemplateProject.replace("{{project}}", data["project"], 1)
    tempTemplateProject = tempTemplateProject.replace("{{for}}", data["for"], 1)
    tempTemplateProject = tempTemplateProject.replace("{{role}}", data["role"], 1)
    tempTemplateProject = tempTemplateProject.replace("{{url}}", url, 1)
    tempTemplateProject = tempTemplateProject.replace("{{grid}}", finalProjectGrid, 1)

    with open("../" + diretorio + ".html", "w") as arquivoProjetoFinal:
      arquivoProjetoFinal.write(tempTemplateProject.encode('utf-8'))

templateIndex = templateIndex.replace("{{name}}", name, 5)
templateIndex = templateIndex.replace("{{about}}", about, 2)
templateIndex = templateIndex.replace("{{grid}}", finalIndexGrid, 1)
templateIndex = templateIndex.replace("{{github}}", github, 1)
templateIndex = templateIndex.replace("{{curriculum}}", curriculum, 1)
templateIndex = templateIndex.replace("{{contact}}", contact, 1)

with open("../index.html", "w") as arquivoIndexFinal:
  arquivoIndexFinal.write(templateIndex.encode('utf-8'))