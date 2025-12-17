---
layout: default
title: Empirical evaluation of the Frank-Wolfe methods for constructing white-box adversarial attacks
---

# Empirical evaluation of the Frank-Wolfe methods for constructing white-box adversarial attacks

**arXiv**: [2512.10936v1](https://arxiv.org/abs/2512.10936) | [PDF](https://arxiv.org/pdf/2512.10936.pdf)

**作者**: Kristina Korotkova, Aleksandr Katrutsa

---

## 💡 一句话要点

**提出改进Frank-Wolfe方法以构建高效白盒对抗攻击，用于评估神经网络对抗鲁棒性。**

**关键词**: `对抗攻击` `Frank-Wolfe方法` `白盒攻击` `神经网络鲁棒性` `数值优化` `投影自由方法`

## 📋 核心要点

1. 核心问题：构建快速有效的对抗攻击以评估神经网络对抗鲁棒性，涉及特定优化问题求解。
2. 方法要点：采用改进的Frank-Wolfe方法（无投影方法）构建白盒对抗攻击，从数值优化角度提升效率与效果。
3. 实验或效果：在MNIST和CIFAR-10数据集上，对逻辑回归、CNN和ViT模型进行数值实验，与基于投影或几何直觉的标准方法比较。

## 📄 摘要（原文）

> The construction of adversarial attacks for neural networks appears to be a crucial challenge for their deployment in various services. To estimate the adversarial robustness of a neural network, a fast and efficient approach is needed to construct adversarial attacks. Since the formalization of adversarial attack construction involves solving a specific optimization problem, we consider the problem of constructing an efficient and effective adversarial attack from a numerical optimization perspective. Specifically, we suggest utilizing advanced projection-free methods, known as modified Frank-Wolfe methods, to construct white-box adversarial attacks on the given input data. We perform a theoretical and numerical evaluation of these methods and compare them with standard approaches based on projection operations or geometrical intuition. Numerical experiments are performed on the MNIST and CIFAR-10 datasets, utilizing a multiclass logistic regression model, the convolutional neural networks (CNNs), and the Vision Transformer (ViT).

