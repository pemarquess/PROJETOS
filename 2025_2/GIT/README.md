# Meu-Projeto

git init
- iniciar novo projeto com git

git add <nome-arquivo> /ou/.
- adiciona os arquivos que estão prontos para serem commitados

git commit -m "mensagem commit"
- commit os arquivos no histórico

git log
- mostra os últimos commits, log de alterações

git status
- como está o estado da nossa ramificação

git diff
- mostra o que foi alterado
- o que tem de alteração na ramificação

git merge
merge de ramificação, mescla ramificações

git branch
- mostra a branch atual

git checkout <nome-branch>
- muda pra essa branch

git branch -b <nome-branch>
- cria uma nova branch a partir da branch atual que estamos

git remote add <nome> <url>
- add um repositório remoto

git push <nome> <nome-branch>
- manda nossas alterações locais para o repositório remoto, pra cada branch

git pull <nome> <nome-branch>
- pega as alterações do repositório remoto e joga pra nossa máquina

git fetch
- atualiza o novo histórico local de acordo com o histórico salvo lá no repositório
- sincronização do local com o remoto
