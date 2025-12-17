---
layout: default
title: AD-SAM: Fine-Tuning the Segment Anything Vision Foundation Model for Autonomous Driving Perception
---

# AD-SAM: Fine-Tuning the Segment Anything Vision Foundation Model for Autonomous Driving Perception

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.27047" target="_blank" class="toolbar-btn">arXiv: 2510.27047v1</a>
    <a href="https://arxiv.org/pdf/2510.27047.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27047v1" 
            onclick="toggleFavorite(this, '2510.27047v1', 'AD-SAM: Fine-Tuning the Segment Anything Vision Foundation Model for Autonomous Driving Perception')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Mario Camarena, Het Patel, Fatemeh Nazari, Evangelos Papalexakis, Mohamadhossein Noruzoliaee, Jia Chen

**分类**: cs.CV

**发布日期**: 2025-10-30

**备注**: Submitted to IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)

---

## 💡 一句话要点

**AD-SAM：微调SAM视觉基础模型，用于自动驾驶感知**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `语义分割` `视觉基础模型` `可变形卷积` `双编码器`

## 📋 核心要点

1. 现有方法难以兼顾自动驾驶场景中全局语义信息和局部空间细节，导致分割精度不足。
2. AD-SAM通过双编码器融合全局语义和局部空间信息，并利用可变形模块对齐异构特征，提升分割性能。
3. 实验表明，AD-SAM在Cityscapes和BDD100K数据集上显著优于SAM、G-SAM和DeepLabV3，且具有更快的学习速度。

## 📝 摘要（中文）

本文提出了自动驾驶分割一切模型（AD-SAM），这是一个为自动驾驶（AD）中的语义分割而微调的视觉基础模型。AD-SAM通过一个双编码器和可变形解码器扩展了分割一切模型（SAM），该解码器专为道路场景的空间和几何复杂性而设计。双编码器通过结合来自SAM的预训练Vision Transformer（ViT-H）的全局语义上下文和来自可训练卷积深度学习骨干网络（即ResNet-50）的局部空间细节来生成多尺度融合表示。一个可变形融合模块对齐跨尺度和对象几何形状的异构特征。解码器使用可变形注意力执行渐进式多阶段细化。训练由混合损失指导，该混合损失集成了Focal、Dice、Lovasz-Softmax和Surface损失，从而提高了语义类平衡、边界精度和优化稳定性。在Cityscapes和Berkeley DeepDrive 100K（BDD100K）基准测试上的实验表明，AD-SAM在分割精度方面超越了SAM、广义SAM（G-SAM）和一个深度学习基线（DeepLabV3）。

## 🔬 方法详解

**问题定义**：自动驾驶场景下的语义分割任务，现有方法如SAM等，在处理道路场景复杂的空间几何结构和多尺度目标时，精度不足，尤其是在兼顾全局语义信息和局部空间细节方面存在挑战。现有方法难以平衡分割精度、泛化能力和计算效率。

**核心思路**：AD-SAM的核心思路是利用双编码器结构，将SAM预训练的ViT-H提供的全局语义信息与ResNet-50提取的局部空间细节进行有效融合。通过可变形融合模块和可变形注意力机制，自适应地对齐和细化不同尺度和几何形状的特征，从而提升分割精度。

**技术框架**：AD-SAM的整体架构包括：1) 双编码器：ViT-H提取全局语义特征，ResNet-50提取局部空间特征；2) 可变形融合模块：对齐和融合来自两个编码器的异构特征；3) 可变形解码器：通过多阶段细化，逐步提升分割精度。训练过程使用混合损失函数，包括Focal Loss、Dice Loss、Lovasz-Softmax Loss和Surface Loss。

**关键创新**：AD-SAM的关键创新在于：1) 双编码器结构，有效融合全局语义和局部空间信息；2) 可变形融合模块和可变形注意力机制，自适应地处理道路场景中复杂的目标几何形状和尺度变化；3) 混合损失函数，平衡语义类、边界精度和优化稳定性。与SAM相比，AD-SAM更专注于自动驾驶场景，通过针对性的架构和优化，显著提升了分割性能。

**关键设计**：双编码器中，ViT-H使用SAM的预训练权重，ResNet-50进行端到端训练。可变形融合模块采用可变形卷积，自适应地调整感受野。解码器使用多层可变形注意力，逐步细化分割结果。混合损失函数中，各种损失的权重需要根据数据集和任务进行调整。训练采用AdamW优化器，学习率根据经验设置。

## 📊 实验亮点

AD-SAM在Cityscapes数据集上实现了68.1%的mIoU，在BDD100K数据集上实现了59.5%的mIoU，分别比SAM、G-SAM和DeepLabV3高出高达+22.9%和+19.2%。AD-SAM具有更强的跨域泛化能力，保留分数为0.87（SAM为0.76），并且学习速度更快，仅需30-40个epoch即可收敛。在仅使用1000个样本的情况下，仍能保持0.607的mIoU，表明其具有很高的数据效率。

## 🎯 应用场景

AD-SAM可应用于自动驾驶汽车的环境感知系统，为车辆提供精确的语义分割结果，从而提高车辆对道路、交通参与者和障碍物的理解能力。这有助于提升自动驾驶系统的安全性、可靠性和智能化水平，并可扩展到其他需要高精度语义分割的领域，如机器人导航、智能交通管理等。

## 📄 摘要（原文）

> This paper presents the Autonomous Driving Segment Anything Model (AD-SAM), a fine-tuned vision foundation model for semantic segmentation in autonomous driving (AD). AD-SAM extends the Segment Anything Model (SAM) with a dual-encoder and deformable decoder tailored to spatial and geometric complexity of road scenes. The dual-encoder produces multi-scale fused representations by combining global semantic context from SAM's pretrained Vision Transformer (ViT-H) with local spatial detail from a trainable convolutional deep learning backbone (i.e., ResNet-50). A deformable fusion module aligns heterogeneous features across scales and object geometries. The decoder performs progressive multi-stage refinement using deformable attention. Training is guided by a hybrid loss that integrates Focal, Dice, Lovasz-Softmax, and Surface losses, improving semantic class balance, boundary precision, and optimization stability. Experiments on the Cityscapes and Berkeley DeepDrive 100K (BDD100K) benchmarks show that AD-SAM surpasses SAM, Generalized SAM (G-SAM), and a deep learning baseline (DeepLabV3) in segmentation accuracy. It achieves 68.1 mean Intersection over Union (mIoU) on Cityscapes and 59.5 mIoU on BDD100K, outperforming SAM, G-SAM, and DeepLabV3 by margins of up to +22.9 and +19.2 mIoU in structured and diverse road scenes, respectively. AD-SAM demonstrates strong cross-domain generalization with a 0.87 retention score (vs. 0.76 for SAM), and faster, more stable learning dynamics, converging within 30-40 epochs, enjoying double the learning speed of benchmark models. It maintains 0.607 mIoU with only 1000 samples, suggesting data efficiency critical for reducing annotation costs. These results confirm that targeted architectural and optimization enhancements to foundation models enable reliable and scalable AD perception.

