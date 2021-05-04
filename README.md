# EJP-RD_standards_and_tools_documentation

### Configuration

**Step 1:**
Place your input `excel` file under `data` folder

**Step 2:**
Please change in the `docker-compose.yml` file the name of the input file. Please make sure file extension is also added to the filename.

```sh
    environment:
      - "INPUT_EXCEL_FILE_NAME=2020-12-04_ALL_standards_tools_ERNs.xlsx"
```
