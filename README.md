# DeepGitStream
Test of Deepnote --> Github --> Streamlit

## Get Streamlit working internally/local in Deepnote
1. Get pip upgraded in Deepnote everytime you run it
    1. Click on Python version (3.11 for data science) dropdown on left side
    2. Choose link to Initiliazation notebook on right side
    3. Make a new line under line 2 with this command: `pip install --upgrade pip`    
2. Get a `requirements.txt` file created
    1. in a code cell in `Notebook1` run: `pip install streamlit==1.45.0`
    2. That should offer a link to move that to the `requirements.txt` file
    3. Add Pillow to it, so it looks like this:
       ```
       streamlit==1.45.0
       Pillow==11.2.1
       ```
    4. Restart the machine, you'll have no warning about pip being old, and these libraries installed
4. In new Deepnote, make `For_Github/Streamlit` folder -> `data` and `assets` folders, add data/images
5. Make simple 3 cell `Analysis` notebook
    ```
    import pandas as pd
    import altair as alt
    ```
    ```
    df_iris = pd.read_csv("For_Github/Streamlit/data/iris.csv")
    df_iris
    ```
    ```
    alt.Chart(df_iris).mark_point().encode(
        x='petalLength',
        y='petalWidth',
        color='variety'
    )
    ```
6. Make Run_streamlit notebook
    ```
    from IPython.core.display import HTML
    import os
    ```
    ```
    display(HTML(f'<h2><a href="https://{os.environ["DEEPNOTE_PROJECT_ID"]}.deepnoteproject.com" target="_blank">Click here</a> to open Streamlit</h2>'))
    print(f"https://" + os.environ["DEEPNOTE_PROJECT_ID"] + ".deepnoteproject.com")
    ```
    ```
    !streamlit run ./MyProject/Streamlit/demo.py --server.port=8080 --browser.serverAddress='0.0.0.0'
    ```
    1. Set working directory to ProjectName
7. Create /Streamlit/demo.py file
8. Try running Run_Streamlit notebook
    1. Streamlit will run, but won't be visible in browser - 403 Forbidden
    2. Next to `Stop machine` button in bottom left, click the `...` button
    3. Slider for Allow Incoming Connections
    4. Try link again, it should show a page :)
    5. Downside, you need to keep restarting Streamlit run command to see new changes in Deepnote

## Get Deepnote connected to github, not best order but we started with notebooks first
1. In your github, create a new repo - siads593_wi24_test
    1. Add a README.md file so there's at least one commit
2. Add Deepnote Integration
    1. on left side, `Integrations` -> `+` -> scroll to Github
    2. Choose newly created repo from drop down, at bottom probably
    3. Notice new `Github` next to new folder icon
    4. Move Streamlit folder from under MyProject to under new folder (siads593_wi24_test)
    5. Delete ProjectName folder
    6. Fix path in Analysis and Run_Streamlit notebooks
    7. Check streamlit page still works
    8. Copy `requirements.txt` file to underneath `Streamlit` folder
3. Push notebooks to GitHub
    1. Click on Clock icon (version) in top right
    2. `Connect GitHub repository` button at very bottom
    3. Choose the new repository you made
    4. Change path where notebooks will be exported to `/Deepnote/`
    5. Add 'main' branch, then `Save`
    6. Click `Commit & push`
    7. Add title, this is only the notebooks, not the other of the files
4. Push the other files to GitHub
    1. Open terminal
    2. cd siads593_wi24_test
    3. git status
    4. git remote -v
    5. git add Streamlit
    6. git pull origin main ~~- will fail~~
    7. ~~git pull --rebase origin main~~
    8. ~~git add *~~
    9. git commit -m "initial add of non-notebook files"
    10. git push origin main ~~--force~~
    11. Now you should see your files in github :)

## Get Streamlit to see github
1. Connect Github to Streamlit Community Cloud servers
    1. Sign in with github account
    2. New App
    3. Find repo in dropdown
    4. Point to `demo.py` file - it's smart
    5. Add optional, pretty subdomain --> Deploy!
    6. Profit!
