# WikiSQL 数据集基础分析报告
> 本报告为描述性统计与基础完整性检查，不直接判定数据集缺陷。

## TRAIN 数据集
- 问题样本数量：56355
### 1. 自然语言问题长度
- count：56355
- mean：11.6377
- median：11
- min：3
- max：44

### 2. SQL 聚合操作分布
- NONE：40606
- COUNT：5114
- MIN：3231
- MAX：3161
- AVG：2201
- SUM：2042

### 3. WHERE 条件数量分布
- 1 个条件：39096
- 2 个条件：13346
- 3 个条件：3019
- 4 个条件：471
- 0 个条件：423

### 4. WHERE 操作符分布
- =：63880
- >：6606
- <：6243

### 5. 基础完整性检查
- missing_question：0
- missing_table_id：0
- missing_sql：0
- invalid_sql_structure：0

### 6. 表格统计
- 表格数量：18585

#### row_count_per_table
- count：18585
- mean：17.0981
- median：11
- min：5
- max：1956

#### column_count_per_table
- count：18585
- mean：6.3498
- median：6
- min：5
- max：44

#### cell_count_per_table
- count：18585
- mean：108.7217
- median：70
- min：25
- max：11600

#### 表格完整性
- duplicate_table_ids：0
- missing_or_invalid_header：0
- malformed_rows：0
- empty_cells：0

### 7. 问题与表格关联
- checked：True
- question_count：56355
- unique_table_count：18585
- missing_table_links：0

---

## DEV 数据集
- 问题样本数量：8421
### 1. 自然语言问题长度
- count：8421
- mean：11.7285
- median：11
- min：3
- max：58

### 2. SQL 聚合操作分布
- NONE：6017
- COUNT：779
- MAX：507
- MIN：468
- AVG：329
- SUM：321

### 3. WHERE 条件数量分布
- 1 个条件：5755
- 2 个条件：2082
- 3 个条件：454
- 4 个条件：66
- 0 个条件：64

### 4. WHERE 操作符分布
- =：9534
- >：1029
- <：982

### 5. 基础完整性检查
- missing_question：0
- missing_table_id：0
- missing_sql：0
- invalid_sql_structure：0

### 6. 表格统计
- 表格数量：2716

#### row_count_per_table
- count：2716
- mean：16.4805
- median：11.0
- min：5
- max：433

#### column_count_per_table
- count：2716
- mean：6.3071
- median：6.0
- min：5
- max：20

#### cell_count_per_table
- count：2716
- mean：102.9878
- median：70.0
- min：25
- max：2165

#### 表格完整性
- duplicate_table_ids：0
- missing_or_invalid_header：0
- malformed_rows：0
- empty_cells：0

### 7. 问题与表格关联
- checked：True
- question_count：8421
- unique_table_count：2716
- missing_table_links：0

---

## TEST 数据集
- 问题样本数量：15878
### 1. 自然语言问题长度
- count：15878
- mean：11.689
- median：11.0
- min：3
- max：43

### 2. SQL 聚合操作分布
- NONE：11324
- COUNT：1455
- MAX：973
- MIN：933
- AVG：606
- SUM：587

### 3. WHERE 条件数量分布
- 1 个条件：10832
- 2 个条件：3879
- 3 个条件：888
- 4 个条件：148
- 0 个条件：131

### 4. WHERE 操作符分布
- =：18114
- >：1927
- <：1805

### 5. 基础完整性检查
- missing_question：0
- missing_table_id：0
- missing_sql：0
- invalid_sql_structure：0

### 6. 表格统计
- 表格数量：5230

#### row_count_per_table
- count：5230
- mean：18.4111
- median：12.0
- min：5
- max：1950

#### column_count_per_table
- count：5230
- mean：6.3193
- median：6.0
- min：5
- max：23

#### cell_count_per_table
- count：5230
- mean：116.1562
- median：70.0
- min：25
- max：11700

#### 表格完整性
- duplicate_table_ids：0
- missing_or_invalid_header：0
- malformed_rows：0
- empty_cells：0

### 7. 问题与表格关联
- checked：True
- question_count：15878
- unique_table_count：5230
- missing_table_links：0

---
