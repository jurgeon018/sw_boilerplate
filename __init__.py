'''








cd ~/projects
mkdir <project_name> 
cd <project_name>
python3 -m venv venv
source venv/bin/activate


mkdir src 
cd src 
git clone git@github.com:jurgeon/<project_name> . 


git clone git@github.com:jurgeon018/box
cp -rp ./boilerplate/* . 


cd sw_shop 
git clone git@github.com:starwayagency/sw_shop .
cd ..


cd sw_blog 
git clone git@github.com:starwayagency/sw_blog .
cd ..


cd sw_liqpay 
git clone git@github.com:starwayagency/sw_liqpay .
cd ..


git add . 
git commit -m 'initial commit'
git push origin master 


pip install -r ./box/core/requirements.txt











'''



