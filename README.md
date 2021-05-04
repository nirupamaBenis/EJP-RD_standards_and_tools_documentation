# EJP-RD_standards_and_tools_documentation

### Configuration

**Step 1:**
Place your input `excel` file under `input` folder

**Step 2:**
Please change in the `docker-compose.yml` file with the input file name. Please make sure file extension is also added to the filename.

```sh
    environment:
      - "INPUT_EXCEL_FILE_NAME=2020-12-04_ALL_standards_tools_ERNs.xlsx"
```

Once you have done above configurations you can run the services by running `docker-compose.yml` file.

```sh
docker-compose up -d