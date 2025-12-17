---
layout: default
title: Zoo3D: Zero-Shot 3D Object Detection at Scene Level
---

# Zoo3D: Zero-Shot 3D Object Detection at Scene Level

**arXiv**: [2511.20253v1](https://arxiv.org/abs/2511.20253) | [PDF](https://arxiv.org/pdf/2511.20253.pdf)

**作者**: Andrey Lemeshko, Bulat Gabdullin, Nikita Drozdov, Anton Konushin, Danila Rukhovich, Maksim Kolodiazhnyi

---

## 💡 一句话要点

**提出Zoo3D实现零训练3D物体检测，解决开放词汇场景理解问题**

**关键词**: `零-shot 3D检测` `开放词汇学习` `图聚类` `视图一致掩码` `训练-free框架` `3D边界框预测`

## 📋 核心要点

1. 核心问题：封闭集方法无法识别未知物体，现有开放词汇检测器仍需训练数据
2. 方法要点：通过2D实例掩码图聚类构建3D框，结合最佳视图选择与视图一致掩码生成进行语义标注
3. 实验效果：在ScanNet200和ARKitScenes基准上实现SOTA，零-shot模式优于自监督方法

## 📄 摘要（原文）

> 3D object detection is fundamental for spatial understanding. Real-world environments demand models capable of recognizing diverse, previously unseen objects, which remains a major limitation of closed-set methods. Existing open-vocabulary 3D detectors relax annotation requirements but still depend on training scenes, either as point clouds or images. We take this a step further by introducing Zoo3D, the first training-free 3D object detection framework. Our method constructs 3D bounding boxes via graph clustering of 2D instance masks, then assigns semantic labels using a novel open-vocabulary module with best-view selection and view-consensus mask generation. Zoo3D operates in two modes: the zero-shot Zoo3D$_0$, which requires no training at all, and the self-supervised Zoo3D$_1$, which refines 3D box prediction by training a class-agnostic detector on Zoo3D$_0$-generated pseudo labels. Furthermore, we extend Zoo3D beyond point clouds to work directly with posed and even unposed images. Across ScanNet200 and ARKitScenes benchmarks, both Zoo3D$_0$ and Zoo3D$_1$ achieve state-of-the-art results in open-vocabulary 3D object detection. Remarkably, our zero-shot Zoo3D$_0$ outperforms all existing self-supervised methods, hence demonstrating the power and adaptability of training-free, off-the-shelf approaches for real-world 3D understanding. Code is available at https://github.com/col14m/zoo3d .

