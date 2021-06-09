from django.shortcuts import render
from django.contrib.auth import authenticate

from django.shortcuts import redirect

from django.db import models


from .models import Player
from .models import Player
from .models import Group
from .models import Game
from .models import GameModel
from .models import CoachParams
# tuto pour avoir acces a des trucs rapidement
# id de l'equipe en cours : request.user.coachparams.currentTeam.id



# Create your views here.
def searchScore(nameColumn,zipRankingNumberIdgameIdgamemodel) -> int: #Prend en paramètre la colonne (dans ModelGame) et nous donne en sortie le score associé à cette colonne. Pour simplifier la fonction en prend aussi le zipRankingNumberIdgameIdgamemodel qui permet d'avoir l'historique des jeux du joueur. L'id du joueur est donné dans le zip
    score = 0
    for rank,number,idGame,idGameModel in zipRankingNumberIdgameIdgamemodel: #A chaque itération on parcour un jeu
        if str(nameColumn) in list(idGameModel):
            if (number == 2): #Dans le cas de deux équipes
                if (rank==1):
                    score += 54
                if (rank == 2):
                    score += 18
                if(rank == 11):
                    score += 36
            if (number == 3): #Dans le cas de trois équipes
                if (rank==1):
                    score += 54
                if (rank == 2):
                    score += 36
                if (rank == 3):
                    score += 18
                if(rank == 111): # On est dans le cas de 1er / 1er / 1er
                    score += 36
                if(rank == 110): # On est dans le cas de 1er / 1er / 2eme
                    score += 45
                if(rank == 220): # On est dans le cas de 1er / 2eme / 2eme
                    score += 27 
            if (number == 4): #Dans le cas de deux équipes
                if (rank==1):
                    score += 54
                if (rank == 2):
                    score += 42
                if (rank == 3):
                    score += 30
                if (rank == 4):
                    score += 18
                if(rank == 1100): # On est dans le cas de 1/1/...
                    score += 48
                if(rank == 3300): # On est dans le cas de 1/2/3/3
                    score += 24
                if(rank == 2220): # On est dans le cas de 1/2/2/2
                    score += 30
                if(rank == 2200): # On est dans le cas de 1/2/2/3
                    score += 36
                if(rank == 1110): # On est dans le cas de 1/1/1/4
                    score += 42
                if(rank == 1111): # On est dans le cas de 1/1/1/1
                    score += 36
    return score


def get_boolean_field_values(model_instance) -> list:
    if not model_instance:
        return None
    listTrueAttribute = []
    data = {}
    for field in model_instance._meta.get_fields():
        if isinstance(field, models.BooleanField):
            data[field.name] = getattr(model_instance, field.name)
            if getattr(model_instance, field.name):
                listTrueAttribute.append(field.name)  
    #return data
    return listTrueAttribute
# my_instance = MyModel.objects.get(id=1234)
# data = get_boolean_field_values(my_instance)

def rankingPlayer(idPlayer):
# On passe en argument l'id du joueur et la fonction nous ressort un zip du classement du joueur associe au nb d'équipe pour chacun des jeux auquels le jouer à participé 
    listRanking = [] # list qui contient le classement du joueur pour chacun de ses matchs.
    listNumberTeam = []
    listIdGame = []
    listOfListTrueGameModel = []
    objIdPlayer = Player.objects.get(id=idPlayer)
    groupsPlayer = Group.objects.filter(player=idPlayer)
    for group in groupsPlayer:
        listRanking.append(int(group.ranking))
        listNumberTeam.append(group.game.numberGroups) #group.game donne l'id du game associé
        listIdGame.append(group.game.id)
        listOfListTrueGameModel.append(get_boolean_field_values(group.game.gameModel))

    #On veut aussi ajouter le nombre d'equipe du jeu associé au classement
    return zip(listRanking[::-1][0:7],listNumberTeam[::-1][0:7],listIdGame[::-1][0:7],listOfListTrueGameModel[::-1][0:7])


# Create your views here.
def ListesEquipes(request):

  # ACCES au variable de session avec request.user et on a acces aux différents attributs de l'utilisateur qui est connécté
    # objects.select_related('country', 'country_state', 'city')
    MyTeams = request.user.coachparams.team.all()
    if request.method == 'POST':
      currentTeamp = int(request.POST.get("currentTeam"))
      request.user.coachparams.currentTeam_id = currentTeamp
      request.user.coachparams.save()
      return redirect ('/NouveauMatch/')
    return render(request, 'ListesEquipes.html',{'MyTeams':MyTeams, 'equipeActuelle' : request.user.coachparams.currentTeam.id})

    #Appuie sur l'équipe et doit ajouter sur la table utilisateur sur la colonne Equipe en cours lel nom de l'équipe qu'il a séléctionné

def JoueursCree(request):
    firstName_lastName = ''
    firstName = ''
    lastName = ''
    weight = ''
    VMA =''
    heigth = ''
    placeOnField = ''
    Remarques = ''
    AfficheJoueurs = Player
    #form = JoueursForm()
    Date_de_naissance = ''
    objectJoueur = ''
    ok=''
    if request.method == "POST":
        if not request.POST.get('heigth'): #On est dans le cas d'un VALIDER
        #if not request.POST.get('firstName_lastName'):
            firstName_lastName = request.POST.get('firstName_lastName').split(" ")

            if(len(firstName_lastName) != 2):
                return redirect('/Equipes/JoueursCree/')
            if(len(firstName_lastName) == 2 ):
                objectJoueur = Player.objects.filter(firstName=str(firstName_lastName[0])).filter(lastName=str(firstName_lastName[1]))
                for joueur in objectJoueur:
                    firstName = str(joueur.firstName)
                    lastName = str(joueur.lastName)
                    weight = str(joueur.weight)
                    VMA = str(joueur.VMA)
                    heigth = str(joueur.heigth)
                    placeOnField = str(joueur.placeOnField)
                    #Date_de_naissance = str(joueur.dateNaissance)
                    #Remarques = str(joueur.Remarques)
        
        
        
        
        else: #On est dans le cas d'un modifier
            if 'statPlayerModif' in request.POST:
                firstName_lastName = [str(firstName),str(lastName)]
                #objectJoueur2 = Player.objects.filter(firstName=str(firstName)).filter(lastName=str(lastName))
                for joueur in Player.objects.filter(firstName="").filter(lastName=""):
                    vghj
                    joueur.weightt = int(request.POST.get('weight'))
                    joueur.VMA = int(request.POST.get('VMA'))
                    joueur.heigth = int(request.POST.get('heigth'))
                    if (request.POST.get('placeOnField') == 'Attaquant' or request.POST.get('placeOnField') == 'Milieu' or request.POST.get('placeOnField') == 'Defenseur' or request.POST.get('placeOnField') == 'Gardien'):
                        joueur.placeOnField = str(request.POST.get('placeOnField'))
                    #joueur.Remarques = str(request.POST.get('Remarques'))
                    joueur.save()
        #form = JoueursForm(request.POST).save() # On sauvegarde dans form le formulaire de Joueurs que l'on a mis dans formStudent

    taille=1
    zipRankingNumberIdgameIdgamemodel = ''
    zipRankingNumberIdgameIdgamemodel2 = ''
    score = 0
    scoreGoalKeeperYes = 0
    scoreGoalKeeperNo = 0
    scoreOffLineYes = 0
    scoreOffLineNo = 0
    scoreSynthetiqueDry = 0
    scoreSynthetiqueWet = 0
    scoreStabiliseDry = 0
    scoreStabiliseWet = 0
    scoreGrassDry = 0
    scoreGrassWet = 0
    scoreOtherField = 0
    scoreGoal11 = 0
    scoreGoal7 = 0
    scoreGoalEmbut = 0
    scoreGoalNone = 0
    scoreGoalOther = 0
    scoreTB1_3 = 0
    scoreTB_2 = 0
    scoreTB_free = 0
    scoreGoalSmall = 0

    #Construction du dictionnaire pour la barre de rechercher

    Players = Player.objects.all()

    persons = []
   
    for player in Players:
        data = {}
        data['name']=str(str(player.firstName)+" "+str(player.lastName))
        persons.append(data)

    if request.method == 'POST':
        if 'statPlayer' in request.POST:
            if not request.POST.get('firstName_lastName'):
                return redirect('/Equipes/JoueursCree/')
            firstName_lastName = request.POST.get('firstName_lastName').strip(" ").title().split(" ") #on retire les espaces en debut et fin de chaine et on ajoute les majuscules au prénom et nom s'ils on ete oublie
            if(len(firstName_lastName)!=2):
                return redirect('/Equipes/JoueursCree/')
            objectJoueur = Player.objects.filter(firstName=str(firstName_lastName[0])).filter(lastName=str(firstName_lastName[1]))
            if not objectJoueur: 
                return redirect('/Equipes/JoueursCree/')
            for joueur in objectJoueur:
                zipRankingNumberIdgameIdgamemodel = rankingPlayer(joueur.id)
                zipRankingNumberIdgameIdgamemodel2 = rankingPlayer(joueur.id)
            for rank,number,idGame,idGameModel in zipRankingNumberIdgameIdgamemodel:
                if (number == 2): #Dans le cas de deux équipes
                    if (rank==1):
                        score += 54
                    if (rank == 2):
                        score += 18
                    if(rank == 11):
                        score += 36
                if (number == 3): #Dans le cas de trois équipes
                    if (rank==1):
                        score += 54
                    if (rank == 2):
                        score += 36
                    if (rank == 3):
                        score += 18
                    if(rank == 111): # On est dans le cas de 1er / 1er / 1er
                        score += 36
                    if(rank == 110): # On est dans le cas de 1er / 1er / 2eme
                        score += 45
                    if(rank == 220): # On est dans le cas de 1er / 2eme / 2eme
                        score += 27 
                if (number == 4): #Dans le cas de deux équipes
                    if (rank==1):
                        score += 54
                    if (rank == 2):
                        score += 42
                    if (rank == 3):
                        score += 30
                    if (rank == 4):
                        score += 18
                    if(rank == 1100): # On est dans le cas de 1/1/...
                        score += 48
                    if(rank == 3300): # On est dans le cas de 1/2/3/3
                        score += 24
                    if(rank == 2220): # On est dans le cas de 1/2/2/2
                        score += 30
                    if(rank == 2200): # On est dans le cas de 1/2/2/3
                        score += 36
                    if(rank == 1110): # On est dans le cas de 1/1/1/4
                        score += 42
                    if(rank == 1111): # On est dans le cas de 1/1/1/1
                        score += 36

        # On met dans la table Player le score du joueur
            if Player.objects.get(id=joueur.id):
                taille = len(list(zip(rankingPlayer(joueur.id))))
                ply = Player.objects.get(id=joueur.id)
                ply.globalScore = score/taille #On fait la moyennHJKKJHJKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKe sur les 7 derniers matchs
                ply.save()
                
            if joueur.id:
                scoreGoalKeeperYes = searchScore('goalKeeperYes', rankingPlayer(joueur.id))
                scoreGoalKeeperNo = searchScore('goalKeeperNo', rankingPlayer(joueur.id))
                scoreOffLineYes = searchScore('offLineYes', rankingPlayer(joueur.id))
                scoreOffLineNo = searchScore('offLineNo', rankingPlayer(joueur.id))
                scoreSynthetiqueDry = searchScore('synthetiqueDry', rankingPlayer(joueur.id))
                scoreSynthetiqueWet = searchScore('synthetiqueWet', rankingPlayer(joueur.id))
                scoreStabiliseDry = searchScore('stabiliseDry', rankingPlayer(joueur.id))
                scoreStabiliseWet = searchScore('stabiliseWet', rankingPlayer(joueur.id))
                scoreGrassDry = searchScore('grassDry', rankingPlayer(joueur.id))
                scoreGrassWet = searchScore('grassWet', rankingPlayer(joueur.id))
                scoreOtherField = searchScore('otherField', rankingPlayer(joueur.id))
                scoreGoal11 = searchScore('goal11', rankingPlayer(joueur.id))
                scoreGoal7 = searchScore('goal7', rankingPlayer(joueur.id))
                scoreGoalEmbut = searchScore('goalEmbut', rankingPlayer(joueur.id))
                scoreGoalNone = searchScore('goalNone', rankingPlayer(joueur.id))
                scoreGoalOther = searchScore('goalOther', rankingPlayer(joueur.id))
                scoreTB1_3 = searchScore('TB1_3', rankingPlayer(joueur.id))
                scoreTB_2 = searchScore('TB_2', rankingPlayer(joueur.id))
                scoreTB_free = searchScore('TB_free', rankingPlayer(joueur.id))
                scoreGoalSmall = searchScore('goalSmall', rankingPlayer(joueur.id))

    return render(request, 'JoueursCrees.html', {'objectJoueur' : objectJoueur, 'firstName':firstName ,'lastName':lastName, 'weight' : weight, 'VMA' : VMA,'heigth' : heigth,'placeOnField' : placeOnField, 'Date_de_naissance' : Date_de_naissance,'Remarques' : Remarques,
    'scoreGoalKeeperYes':scoreGoalKeeperYes,
    'scoreGoalSmall':scoreGoalSmall,
    'scoreTB_free':scoreTB_free,
    'scoreTB_2':scoreTB_2,
    'scoreTB1_3':scoreTB1_3,
    'scoreGoalOther':scoreGoalOther,
    'scoreGoalNone':scoreGoalNone,
    'scoreGoalEmbut':scoreGoalEmbut,
    'scoreGoal7':scoreGoal7,
    'scoreGoal11':scoreGoal11,
    'scoreOtherField':scoreOtherField,
    'scoreGrassWet':scoreGrassWet,
    'scoreGrassDry':scoreGrassDry,
    'scoreStabiliseWet':scoreStabiliseWet,
    'scoreStabiliseDry':scoreStabiliseDry,
    'scoreSynthetiqueWet':scoreSynthetiqueWet,
    'scoreSynthetiqueDry':scoreSynthetiqueDry,
    'scoreOffLineNo':scoreOffLineNo,
    'scoreOffLineYes':scoreOffLineYes,
    'scoreGoalKeeperNo':scoreGoalKeeperNo,
    'zipRankingNumberIdgameIdgamemodel':zipRankingNumberIdgameIdgamemodel2 ,
     'score':score/taille,

     'persons':persons})

def StatistiqueEquipe(request):

    # MyTeams = request.user.coachparams.team.all()
    # taille=1
    # zipRankingNumberIdgameIdgamemodel = ''
    # zipRankingNumberIdgameIdgamemodel2 = ''
    # score = 0
    # scoreGoalKeeperYes = 0
    # scoreGoalKeeperNo = 0
    # scoreOffLineYes = 0
    # scoreOffLineNo = 0
    # scoreSynthetiqueDry = 0
    # scoreSynthetiqueWet = 0
    # scoreStabiliseDry = 0
    # scoreStabiliseWet = 0
    # scoreGrassDry = 0
    # scoreGrassWet = 0
    # scoreOtherField = 0
    # scoreGoal11 = 0
    # scoreGoal7 = 0
    # scoreGoalEmbut = 0
    # scoreGoalNone = 0
    # scoreGoalOther = 0
    # scoreTB1_3 = 0
    # scoreTB_2 = 0
    # scoreTB_free = 0
    # scoreGoalSmall = 0

    # #Construction du dictionnaire pour la barre de rechercher

    # Players = Player.objects.all()

    # persons = []
   
   # Récupération de l'id de la currentTeam

    idUser = request.user.id
    idTeam = CoachParams.objects.get(user=idUser).currentTeam.id


    # for player in Players:
    #     data = {}
    #     data['name']=str(str(player.firstName)+" "+str(player.lastName))
    #     persons.append(data)
    # if request.method == 'POST':
    #     if 'StatTeam' in request.POST:
    #         return redirect('/StatistiqueGame/idTeam='+str(request.POST.get('currentTeam')))

    listScore = []
    listFirstName_LastName = []
    data = {}
    searchCara = ''
    dataCara = {}
    Players = Player.objects.filter(team=idTeam)
    for player in Players:
        data[str(str(player.firstName)+str(player.lastName))] = int(player.globalScore)
    
    dataSorted = sorted(data.items(), key=lambda t: t[1])

    for name,score in dataSorted:
        listScore.append(int(score))
        listFirstName_LastName.append(str(name))

    ZipScoreName = zip(listScore[::-1],listFirstName_LastName[::-1]) 
    if request.method == 'POST':
        listScore = []
        listFirstName_LastName = []
        searchCara = str(request.POST.get("searchCara"))
        dataCara = {}
        for player in Players:
            dataCara[str(str(player.firstName)+str(player.lastName))] = int(searchScore(searchCara, rankingPlayer(player.id)))
    
        dataSorted = sorted(dataCara.items(), key=lambda t: t[1])

        for name,score in dataSorted:
            listScore.append(int(score))
            listFirstName_LastName.append(str(name)) 
        ZipScoreName = zip(listScore[::-1],listFirstName_LastName[::-1])
    
    return render(request, 'FeedbackJeuxBaseTeam.html', {'searchCara':searchCara,'dataCara':dataCara,'ZipScoreName':ZipScoreName})

    # return render(request, 'StatistiqueEquipe.html',
    # {'scoreGoalKeeperYes':scoreGoalKeeperYes,
    # 'scoreGoalSmall':scoreGoalSmall,
    # 'scoreTB_free':scoreTB_free,
    # 'scoreTB_2':scoreTB_2,
    # 'scoreTB1_3':scoreTB1_3,
    # 'scoreGoalOther':scoreGoalOther,
    # 'scoreGoalNone':scoreGoalNone,
    # 'scoreGoalEmbut':scoreGoalEmbut,
    # 'scoreGoal7':scoreGoal7,
    # 'scoreGoal11':scoreGoal11,
    # 'scoreOtherField':scoreOtherField,
    # 'scoreGrassWet':scoreGrassWet,
    # 'scoreGrassDry':scoreGrassDry,
    # 'scoreStabiliseWet':scoreStabiliseWet,
    # 'scoreStabiliseDry':scoreStabiliseDry,
    # 'scoreSynthetiqueWet':scoreSynthetiqueWet,
    # 'scoreSynthetiqueDry':scoreSynthetiqueDry,
    # 'scoreOffLineNo':scoreOffLineNo,
    # 'scoreOffLineYes':scoreOffLineYes,
    # 'scoreGoalKeeperNo':scoreGoalKeeperNo,
    # 'zipRankingNumberIdgameIdgamemodel':zipRankingNumberIdgameIdgamemodel2 ,
    #  'score':score/taille,
     
    #  'MyTeams':MyTeams,
    #  'persons':persons})