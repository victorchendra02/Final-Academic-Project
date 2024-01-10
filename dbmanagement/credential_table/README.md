# DBManagement:
This is to INSERT ROW for credential

1. Create new table first
```sql
CREATE TABLE IF NOT EXISTS `credential_table` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `datetime` timestamp NULL DEFAULT NULL,
    `credential` varchar(255) DEFAULT NULL,
    `is_active` tinyint(1) DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `credential` (`credential`)
);
```
2. Paste your list of credential in `credential_list.txt`, then execute `insert_credential.py`


## How to run:
1. Open terminal (in VS CODE simply `CTRL + SHIFT + C`)
2. Then copy this

```bash
conda activate artofproblemsolving
cd dbmanagement
cd credential_table
python -u insert_credential.py
```