{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f6e5354c-c79c-4aea-8376-f14bcce4fe4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array 1: [10 20 30 40]\n",
      "Array 2: [ 5 10 15 20]\n",
      "Addition: [15 30 45 60]\n",
      "Subtraction: [ 5 10 15 20]\n",
      "Multiplication: [ 50 200 450 800]\n",
      "Division: [2. 2. 2. 2.]\n",
      "Modulus: [0 0 0 0]\n",
      "Exponentiation (square): [ 100  400  900 1600]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "array1 = np.array([10, 20, 30, 40])\n",
    "array2 = np.array([5, 10, 15, 20])\n",
    "\n",
    "\n",
    "addition = array1 + array2        \n",
    "subtraction = array1 - array2     \n",
    "multiplication = array1 * array2  \n",
    "division = array1 / array2       \n",
    "modulus = array1 % array2        \n",
    "exponentiation = array1 ** 2      \n",
    "\n",
    "\n",
    "print(\"Array 1:\", array1)\n",
    "print(\"Array 2:\", array2)\n",
    "print(\"Addition:\", addition)\n",
    "print(\"Subtraction:\", subtraction)\n",
    "print(\"Multiplication:\", multiplication)\n",
    "print(\"Division:\", division)\n",
    "print(\"Modulus:\", modulus)\n",
    "print(\"Exponentiation (square):\", exponentiation)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15a21d64-8b2b-4ade-af4e-bffd9e8ff759",
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
