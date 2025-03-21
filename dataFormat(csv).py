{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "31f9a9c8-0afd-4570-b5f3-93e656caf3ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "21b15013-cd81-4126-a568-3524902564cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   sepal_length  sepal_width  petal_length  petal_width species\n",
      "0           5.1          3.5           1.4          0.2  setosa\n",
      "1           4.9          3.0           1.4          0.2  setosa\n",
      "2           4.7          3.2           1.3          0.2  setosa\n",
      "3           4.6          3.1           1.5          0.2  setosa\n",
      "4           5.0          3.6           1.4          0.2  setosa\n"
     ]
    }
   ],
   "source": [
    "url = \"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv\"\n",
    "\n",
    "# Read CSV file\n",
    "df = pd.read_csv(url)\n",
    "print(df.head())  # Display first five rows\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "85b7d128-0310-44e2-9bcd-5d12d9d738f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV file saved successfully.\n"
     ]
    }
   ],
   "source": [
    "df.to_csv(\"iris_output.csv\", index=False)  # Save without index\n",
    "print(\"CSV file saved successfully.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "aa516a17-2acc-4b20-9561-11932ed59985",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   sepal_length  sepal_width  petal_length  petal_width species\n",
      "0           5.1          3.5           1.4          0.2  setosa\n",
      "1           4.9          3.0           1.4          0.2  setosa\n",
      "2           4.7          3.2           1.3          0.2  setosa\n",
      "3           4.6          3.1           1.5          0.2  setosa\n",
      "4           5.0          3.6           1.4          0.2  setosa\n"
     ]
    }
   ],
   "source": [
    "df.to_csv(\"iris_tab_delimited.txt\", sep='\\t', index=False)  # Save as tab-separated file\n",
    "\n",
    "# Read the tab-delimited file using read_table\n",
    "df_tab = pd.read_table(\"iris_tab_delimited.txt\", sep='\\t')\n",
    "print(df_tab.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "530056d5-f826-439a-b6ef-2dff4db78cf0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:anaconda3]",
   "language": "python",
   "name": "conda-env-anaconda3-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
