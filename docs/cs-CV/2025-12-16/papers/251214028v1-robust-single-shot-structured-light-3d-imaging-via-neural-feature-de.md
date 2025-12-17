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

**提出基于神经特征解码的单次结构光三维成像方法，以提升在遮挡、精细结构和非朗伯表面等挑战场景下的鲁棒性。**

**关键词**: `单次结构光` `三维成像` `神经特征匹配` `深度估计` `合成数据训练` `特征空间解码` `鲁棒性提升` `室内场景`

## 📋 核心要点

1. 传统单次结构光方法依赖像素域匹配，在遮挡、精细结构或非朗伯表面等复杂场景下鲁棒性不足，导致深度估计精度下降。
2. 提出基于神经特征解码的框架，在特征空间而非像素域进行对应匹配，并引入深度细化模块，结合几何先验和大规模单目深度模型先验提升性能。
3. 仅用合成数据训练，方法在真实室内场景中泛化良好，处理多种图案类型无需重新训练，性能优于商业结构光系统和被动立体RGB深度估计方法。

## 📝 摘要（中文）

本文研究了单次结构光系统在主动三维成像中的应用，这类系统广泛应用于苹果Face ID和英特尔RealSense等商业三维传感设备。传统的结构光方法通常通过像素域匹配算法解码深度对应关系，导致在遮挡、精细结构细节和非朗伯表面等挑战场景下鲁棒性有限。受神经特征匹配最新进展的启发，我们提出了一种基于学习的结构光解码框架，在特征空间而非脆弱的像素域执行鲁棒的对应匹配。我们的方法从投影图案和捕获的红外图像中提取神经特征，通过在特征空间中构建代价体积显式地结合其几何先验，相比像素域解码方法实现了显著的性能提升。为进一步提高深度质量，我们引入了一个深度细化模块，利用大规模单目深度估计模型的强先验，改善精细细节恢复和全局结构一致性。为促进有效学习，我们开发了一个基于物理的结构光渲染流程，生成了近百万个包含室内环境中多样物体和材料的合成图案-图像对。实验表明，我们的方法仅使用多种结构光图案的合成数据进行训练，就能很好地泛化到真实世界室内环境，无需重新训练即可有效处理各种图案类型，并始终优于商业结构光系统和基于被动立体RGB的深度估计方法。项目页面：https://namisntimpot.github.io/NSLweb/。

## 🔬 方法详解

整体框架包括神经特征提取、特征空间代价体积构建和深度细化模块。首先，从投影图案和捕获的红外图像中提取神经特征，替代传统像素域匹配。关键创新在于在特征空间中构建代价体积，显式地结合几何先验，实现更鲁棒的对应匹配。与现有方法的主要区别在于：传统方法依赖像素级匹配，易受噪声和场景复杂性影响；而本方法通过深度学习在特征空间进行匹配，提升了在挑战场景下的鲁棒性，并利用大规模单目深度模型的先验进行深度细化，进一步优化细节和全局结构。

## 📊 实验亮点

实验显示，方法在合成和真实数据上均优于传统像素域解码，深度估计误差显著降低；泛化能力强，仅用合成数据训练即可处理真实室内场景和多种图案类型；在遮挡、精细结构等挑战场景下，性能提升尤为明显，优于苹果Face ID和英特尔RealSense等商业系统。

## 🎯 应用场景

该研究可应用于消费电子（如智能手机面部识别、增强现实）、工业检测（如精密零件三维扫描）、机器人导航（如环境感知与避障）等领域，提升三维成像在复杂场景下的可靠性和精度，具有广泛的商业和工业价值。

## 📄 摘要（原文）

> We consider the problem of active 3D imaging using single-shot structured light systems, which are widely employed in commercial 3D sensing devices such as Apple Face ID and Intel RealSense. Traditional structured light methods typically decode depth correspondences through pixel-domain matching algorithms, resulting in limited robustness under challenging scenarios like occlusions, fine-structured details, and non-Lambertian surfaces. Inspired by recent advances in neural feature matching, we propose a learning-based structured light decoding framework that performs robust correspondence matching within feature space rather than the fragile pixel domain. Our method extracts neural features from the projected patterns and captured infrared (IR) images, explicitly incorporating their geometric priors by building cost volumes in feature space, achieving substantial performance improvements over pixel-domain decoding approaches. To further enhance depth quality, we introduce a depth refinement module that leverages strong priors from large-scale monocular depth estimation models, improving fine detail recovery and global structural coherence. To facilitate effective learning, we develop a physically-based structured light rendering pipeline, generating nearly one million synthetic pattern-image pairs with diverse objects and materials for indoor settings. Experiments demonstrate that our method, trained exclusively on synthetic data with multiple structured light patterns, generalizes well to real-world indoor environments, effectively processes various pattern types without retraining, and consistently outperforms both commercial structured light systems and passive stereo RGB-based depth estimation methods. Project page: https://namisntimpot.github.io/NSLweb/.

