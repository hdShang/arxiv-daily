---
layout: default
title: Robust Single-shot Structured Light 3D Imaging via Neural Feature Decoding
---

# Robust Single-shot Structured Light 3D Imaging via Neural Feature Decoding

**arXiv**: [2512.14028v1](https://arxiv.org/abs/2512.14028) | [PDF](https://arxiv.org/pdf/2512.14028.pdf)

**作者**: Jiaheng Li, Qiyu Dai, Lihan Li, Praneeth Chakravarthula, He Sun, Baoquan Chen, Wenzheng Chen

**分类**: cs.CV

**发布日期**: 2025-12-16

**🔗 代码/项目**: [PROJECT_PAGE](https://namisntimpot.github.io/NSLweb/)

---

## 💡 一句话要点

**提出基于神经特征解码的单次结构光3D成像方法，以提升在遮挡、精细结构和非朗伯表面等挑战场景下的鲁棒性。**

🎯 **匹配领域**: **深度估计** **视觉里程计** **强化学习**

**关键词**: `单次结构光` `神经特征解码` `3D成像` `深度估计` `特征空间匹配` `合成数据训练` `鲁棒性提升` `室内场景`

## 📋 核心要点

1. 传统结构光方法依赖像素域匹配，在遮挡、精细结构或非朗伯表面等复杂场景下鲁棒性不足，导致深度估计精度受限。
2. 提出基于神经特征解码的框架，在特征空间进行对应匹配，并引入深度细化模块，结合几何先验和大规模单目深度模型提升性能。
3. 实验显示，该方法仅用合成数据训练，能泛化到真实室内场景，处理多种图案类型，性能优于商业系统和被动立体RGB方法。

## 📝 摘要（中文）

本文研究了单次结构光系统在主动3D成像中的应用，这类系统广泛应用于苹果Face ID和英特尔RealSense等商业3D传感设备。传统结构光方法通常通过像素域匹配算法解码深度对应关系，导致在遮挡、精细结构细节和非朗伯表面等挑战场景下鲁棒性有限。受神经特征匹配最新进展的启发，我们提出了一种基于学习的结构光解码框架，在特征空间而非脆弱的像素域执行鲁棒的对应匹配。我们的方法从投影图案和捕获的红外图像中提取神经特征，通过在特征空间中构建代价体积显式地结合几何先验，相比像素域解码方法实现了显著的性能提升。为进一步提高深度质量，我们引入了深度细化模块，利用大规模单目深度估计模型的强先验，改善精细细节恢复和全局结构一致性。为促进有效学习，我们开发了基于物理的结构光渲染流程，生成了近百万个包含室内场景中多样物体和材质的合成图案-图像对。实验表明，我们的方法仅使用多种结构光图案的合成数据进行训练，能很好地泛化到真实室内环境，无需重新训练即可有效处理各种图案类型，并始终优于商业结构光系统和基于被动立体RGB的深度估计方法。项目页面：https://namisntimpot.github.io/NSLweb/。

## 🔬 方法详解

整体框架包括神经特征提取、特征空间代价体积构建和深度细化模块。关键技术创新点在于将结构光解码从像素域迁移到特征空间，通过提取投影图案和红外图像的神经特征，并构建代价体积来显式结合几何先验，从而提升匹配鲁棒性。与现有方法的主要区别在于：传统方法依赖像素级匹配，易受噪声和场景复杂性影响；而本方法利用学习到的特征进行匹配，更适应挑战场景，同时通过深度细化模块整合外部深度先验，进一步优化细节和全局结构。

## 📊 实验亮点

实验结果表明，该方法在合成和真实数据上均优于传统像素域解码方法，能有效处理遮挡、精细细节和非朗伯表面，性能提升显著，且仅用合成数据训练即可泛化到真实场景，无需针对不同图案重新训练。

## 🎯 应用场景

该研究可应用于消费电子3D传感（如人脸识别、增强现实）、工业检测、机器人导航和虚拟现实等领域，提升在复杂环境下的深度感知精度和鲁棒性，具有实际商业价值。

## 📄 摘要（原文）

> We consider the problem of active 3D imaging using single-shot structured light systems, which are widely employed in commercial 3D sensing devices such as Apple Face ID and Intel RealSense. Traditional structured light methods typically decode depth correspondences through pixel-domain matching algorithms, resulting in limited robustness under challenging scenarios like occlusions, fine-structured details, and non-Lambertian surfaces. Inspired by recent advances in neural feature matching, we propose a learning-based structured light decoding framework that performs robust correspondence matching within feature space rather than the fragile pixel domain. Our method extracts neural features from the projected patterns and captured infrared (IR) images, explicitly incorporating their geometric priors by building cost volumes in feature space, achieving substantial performance improvements over pixel-domain decoding approaches. To further enhance depth quality, we introduce a depth refinement module that leverages strong priors from large-scale monocular depth estimation models, improving fine detail recovery and global structural coherence. To facilitate effective learning, we develop a physically-based structured light rendering pipeline, generating nearly one million synthetic pattern-image pairs with diverse objects and materials for indoor settings. Experiments demonstrate that our method, trained exclusively on synthetic data with multiple structured light patterns, generalizes well to real-world indoor environments, effectively processes various pattern types without retraining, and consistently outperforms both commercial structured light systems and passive stereo RGB-based depth estimation methods. Project page: https://namisntimpot.github.io/NSLweb/.

