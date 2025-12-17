---
layout: default
title: Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views
---

# Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views

**arXiv**: [2512.10369v1](https://arxiv.org/abs/2512.10369) | [PDF](https://arxiv.org/pdf/2512.10369.pdf)

**作者**: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian

---

## 💡 一句话要点

**提出CoherentGS框架，利用双先验策略从稀疏和运动模糊图像实现高保真3D重建。**

**关键词**: `3D高斯泼溅` `稀疏视图重建` `运动模糊处理` `双先验策略` `扩散模型` `去模糊网络`

## 📋 核心要点

1. 核心问题：稀疏和运动模糊图像导致3D高斯泼溅重建失败，形成恶性循环。
2. 方法要点：结合去模糊网络和扩散模型的双先验策略，辅以一致性引导相机探索和深度正则化。
3. 实验或效果：在合成和真实场景上，使用少至3、6、9个输入视图，性能显著优于现有方法。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a state-of-the-art method for novel view synthesis. However, its performance heavily relies on dense, high-quality input imagery, an assumption that is often violated in real-world applications, where data is typically sparse and motion-blurred. These two issues create a vicious cycle: sparse views ignore the multi-view constraints necessary to resolve motion blur, while motion blur erases high-frequency details crucial for aligning the limited views. Thus, reconstruction often fails catastrophically, with fragmented views and a low-frequency bias. To break this cycle, we introduce CoherentGS, a novel framework for high-fidelity 3D reconstruction from sparse and blurry images. Our key insight is to address these compound degradations using a dual-prior strategy. Specifically, we combine two pre-trained generative models: a specialized deblurring network for restoring sharp details and providing photometric guidance, and a diffusion model that offers geometric priors to fill in unobserved regions of the scene. This dual-prior strategy is supported by several key techniques, including a consistency-guided camera exploration module that adaptively guides the generative process, and a depth regularization loss that ensures geometric plausibility. We evaluate CoherentGS through both quantitative and qualitative experiments on synthetic and real-world scenes, using as few as 3, 6, and 9 input views. Our results demonstrate that CoherentGS significantly outperforms existing methods, setting a new state-of-the-art for this challenging task. The code and video demos are available at https://potatobigroom.github.io/CoherentGS/.

