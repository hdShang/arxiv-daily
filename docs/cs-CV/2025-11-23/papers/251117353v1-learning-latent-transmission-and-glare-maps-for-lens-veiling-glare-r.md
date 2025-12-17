---
layout: default
title: Learning Latent Transmission and Glare Maps for Lens Veiling Glare Removal
---

# Learning Latent Transmission and Glare Maps for Lens Veiling Glare Removal

**arXiv**: [2511.17353v1](https://arxiv.org/abs/2511.17353) | [PDF](https://arxiv.org/pdf/2511.17353.pdf)

**作者**: Xiaolong Qian, Qi Jiang, Lei Sun, Zongxi Yu, Kailun Yang, Peixuan Wu, Jiacheng Zhou, Yao Gao, Yaoguang Ma, Ming-Hsuan Yang, Kaiwei Wang

---

## 💡 一句话要点

**提出VeilGen和DeVeiler以解决紧凑光学系统中的杂散光去除问题**

**关键词**: `杂散光去除` `生成模型` `无监督学习` `光学系统恢复` `潜在图估计`

## 📋 核心要点

1. 紧凑光学系统因杂散光导致图像退化，传统散射模型难以拟合
2. VeilGen无监督学习潜在传输和眩光图，结合SD先验生成配对数据
3. DeVeiler利用潜在图指导恢复，实验显示优于现有方法的性能

## 📄 摘要（原文）

> Beyond the commonly recognized optical aberrations, the imaging performance of compact optical systems-including single-lens and metalens designs-is often further degraded by veiling glare caused by stray-light scattering from non-ideal optical surfaces and coatings, particularly in complex real-world environments. This compound degradation undermines traditional lens aberration correction yet remains underexplored. A major challenge is that conventional scattering models (e.g., for dehazing) fail to fit veiling glare due to its spatial-varying and depth-independent nature. Consequently, paired high-quality data are difficult to prepare via simulation, hindering application of data-driven veiling glare removal models. To this end, we propose VeilGen, a generative model that learns to simulate veiling glare by estimating its underlying optical transmission and glare maps in an unsupervised manner from target images, regularized by Stable Diffusion (SD)-based priors. VeilGen enables paired dataset generation with realistic compound degradation of optical aberrations and veiling glare, while also providing the estimated latent optical transmission and glare maps to guide the veiling glare removal process. We further introduce DeVeiler, a restoration network trained with a reversibility constraint, which utilizes the predicted latent maps to guide an inverse process of the learned scattering model. Extensive experiments on challenging compact optical systems demonstrate that our approach delivers superior restoration quality and physical fidelity compared with existing methods. These suggest that VeilGen reliably synthesizes realistic veiling glare, and its learned latent maps effectively guide the restoration process in DeVeiler. All code and datasets will be publicly released at https://github.com/XiaolongQian/DeVeiler.

