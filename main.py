import uvicorn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port="8008", reload=True, workers=3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
