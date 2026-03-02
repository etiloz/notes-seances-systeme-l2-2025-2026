# exercice supplementaire: ecrire un programme `timeout.py cmd delay`
# qui lance la commande dans un fils et tue le fils au bout de delay 
# s'il n'a pas encore terminé

# indices: voir photo
# utiliser signal.alarm pour programmer un minuteur dans le père
# installer un handler dans le père pour réagir à sigalarm
# envoyer sigkill au fils depuis le handler

