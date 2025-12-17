---
layout: default
title: Features Emerge as Discrete States: The First Application of SAEs to 3D Representations
---

# Features Emerge as Discrete States: The First Application of SAEs to 3D Representations

**arXiv**: [2512.11263v1](https://arxiv.org/abs/2512.11263) | [PDF](https://arxiv.org/pdf/2512.11263.pdf)

**作者**: Albert Miao, Chenliang Zhou, Jiawei Zhou, Cengiz Oztireli

---

## 💡 一句话要点

**首次将稀疏自编码器应用于3D表示，揭示特征以离散状态涌现并解释模型行为。**

**关键词**: `稀疏自编码器` `3D表示学习` `特征分解` `离散状态空间` `相变分析` `VAE重建`

## 📋 核心要点

1. 核心问题：稀疏自编码器在文本域外应用有限，阻碍特征分解理论探索。
2. 方法要点：分析3D重建VAE在Objaverse数据集上的特征，发现离散而非连续编码。
3. 实验或效果：观察到相变驱动离散状态空间，解释位置编码偏好和损失行为等现象。

## 📄 摘要（原文）

> Sparse Autoencoders (SAEs) are a powerful dictionary learning technique for decomposing neural network activations, translating the hidden state into human ideas with high semantic value despite no external intervention or guidance. However, this technique has rarely been applied outside of the textual domain, limiting theoretical explorations of feature decomposition. We present the \textbf{first application of SAEs to the 3D domain}, analyzing the features used by a state-of-the-art 3D reconstruction VAE applied to 53k 3D models from the Objaverse dataset. We observe that the network encodes discrete rather than continuous features, leading to our key finding: \textbf{such models approximate a discrete state space, driven by phase-like transitions from feature activations}. Through this state transition framework, we address three otherwise unintuitive behaviors -- the inclination of the reconstruction model towards positional encoding representations, the sigmoidal behavior of reconstruction loss from feature ablation, and the bimodality in the distribution of phase transition points. This final observation suggests the model \textbf{redistributes the interference caused by superposition to prioritize the saliency of different features}. Our work not only compiles and explains unexpected phenomena regarding feature decomposition, but also provides a framework to explain the model's feature learning dynamics. The code and dataset of encoded 3D objects will be available on release.

