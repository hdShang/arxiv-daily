---
layout: default
title: Minimizing Layerwise Activation Norm Improves Generalization in Federated Learning
---

# Minimizing Layerwise Activation Norm Improves Generalization in Federated Learning

**arXiv**: [2512.08314v1](https://arxiv.org/abs/2512.08314) | [PDF](https://arxiv.org/pdf/2512.08314.pdf)

**作者**: M Yashwanth, Gaurav Kumar Nayak, Harsh Rangwani, Arya Singh, R. Venkatesh Babu, Anirban Chakraborty

---

## 💡 一句话要点

**提出MAN正则化以提升联邦学习中模型的泛化性能**

**关键词**: `联邦学习` `泛化性能` `平坦最小值` `Hessian特征值` `激活范数正则化`

## 📋 核心要点

1. 联邦学习易收敛至尖锐最小值，损害模型泛化能力
2. 通过最小化层激活范数约束Hessian特征值，确保平坦最小值
3. 在现有FL技术上应用，显著提升性能，达到新SOTA

## 📄 摘要（原文）

> Federated Learning (FL) is an emerging machine learning framework that enables multiple clients (coordinated by a server) to collaboratively train a global model by aggregating the locally trained models without sharing any client's training data. It has been observed in recent works that learning in a federated manner may lead the aggregated global model to converge to a 'sharp minimum' thereby adversely affecting the generalizability of this FL-trained model. Therefore, in this work, we aim to improve the generalization performance of models trained in a federated setup by introducing a 'flatness' constrained FL optimization problem. This flatness constraint is imposed on the top eigenvalue of the Hessian computed from the training loss. As each client trains a model on its local data, we further re-formulate this complex problem utilizing the client loss functions and propose a new computationally efficient regularization technique, dubbed 'MAN,' which Minimizes Activation's Norm of each layer on client-side models. We also theoretically show that minimizing the activation norm reduces the top eigenvalue of the layer-wise Hessian of the client's loss, which in turn decreases the overall Hessian's top eigenvalue, ensuring convergence to a flat minimum. We apply our proposed flatness-constrained optimization to the existing FL techniques and obtain significant improvements, thereby establishing new state-of-the-art.

