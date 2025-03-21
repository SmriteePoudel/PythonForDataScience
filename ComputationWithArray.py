{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6e45b808-c32f-46e4-8f39-116402f6e349",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Array:\n",
      " [[10 20 30]\n",
      " [40 50 60]\n",
      " [70 80 90]]\n",
      "Element at row 1, column 2: 60\n",
      "First row: [10 20 30]\n",
      "Second column: [20 50 80]\n",
      "Extract a sub-array (first two rows, first two columns):\n",
      " [[10 20]\n",
      " [40 50]]\n",
      "Elements greater than 50: [60 70 80 90]\n",
      "Rows 0 and 2:\n",
      " [[10 20 30]\n",
      " [70 80 90]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "array = np.array([[10, 20, 30], \n",
    "                  [40, 50, 60], \n",
    "                  [70, 80, 90]])\n",
    "\n",
    "\n",
    "print(\"Original Array:\\n\", array)\n",
    "\n",
    "# Accessing individual elements\n",
    "print(\"Element at row 1, column 2:\", array[1, 2]) \n",
    "\n",
    "# Accessing a full row\n",
    "print(\"First row:\", array[0])  \n",
    "\n",
    "# Accessing a full column\n",
    "print(\"Second column:\", array[:, 1])  \n",
    "\n",
    "# Step 3: Perform Slicing\n",
    "print(\"Extract a sub-array (first two rows, first two columns):\\n\", array[:2, :2])\n",
    "\n",
    "# Step 4: Advanced Indexing\n",
    "# Boolean indexing (Extract elements greater than 50)\n",
    "print(\"Elements greater than 50:\", array[array > 50])\n",
    "\n",
    "# Fancy Indexing (Select specific rows)\n",
    "print(\"Rows 0 and 2:\\n\", array[[0, 2]])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad010ef9-369d-4460-941f-8d12e7dc79ae",
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
