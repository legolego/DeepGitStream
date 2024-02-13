# DeepGitStream
Test of Deepnote --> Github --> Streamlit

## Get Streamlit working internally/local in Deepnote
1. In new Deepnote, make ProjectName/Streamlit folder -> data and assets folder, add data/images
2. !pip install --upgrade pip in init.ipynb
3. Make simple Analysis notebook
    1. pandas
    2. altair
    3. iris.csv
4. Make Run_streamlit notebook
    1. Set working directory to ProjectName
    2. !pip install streamlit
    3. click to add it to requirements.txt
    4. Can add "pip install --upgrade pip" to Init notebook.
5. Create /Streamlit/demo.py file
6. Try running Run_Streamlit notebook
    1. Streamlit will run, but won't be visible in browser - 403 Forbidden
    2. Click on Deepnote Environment towrds bottow left
    3. Slider for Allow Incoming Connections
    4. Try link again, it should show a page :)
    5. Downside, you need to keep restarting Streamlit run command to see new changes in Deepnote

## Get Deepnote connected to github, not best order but we started with notebooks first
1. In your github, create a new repo - siads593_wi24_test
    1. Add a README.md file so there's at least one commit
2. Add Deepnote Integration
    1. on left side, click Integrations -> scroll to Github
    2. Choose newly created repo from drop down, at bottom probably
    3. Notice new icon
    4. Move Streamlit folder from under ProjectNAme to under new folder (siads593_wi24_test)
    5. Delete ProjectName folder
    6. Fix path in Analysis notebook
    7. Change working directory of Run_Streamlit notebook
    8. Check streamlit page still works
3. Push notebooks to git
    1. Click on Clock icon (version) in top right
    2. Export to Git button at very bottom
    3. Change path where notebooks will be exported to /Deepnote
    4. Add 'main' branch
    5. Click commit & push
4. Push rest of files to github
    1. Open terminal
    2. cd siads593_wi24_test
    3. git init
    4. git remote -v
    5. git pull origin main - will fail
    6. git pull --rebase origin main
    7. git add *
    8. git commit -m "initial add of non-notebook files"
    9. git push origin <your_branch_name> --force
    10. Now you shoudl see your files in github :)

## Get Streamlit to see github
1. Connect Github to Streamlit Community Cloud servers
    1. Sign in with github account
    2. New App
    3. Find repo
    4. Point to Main file path - it's smart
    5. Add optional, pretty subdomain --> Deploy!
    6. Profit!
