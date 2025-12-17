---
layout: default
title: EGD-YOLO: A Lightweight Multimodal Framework for Robust Drone-Bird Discrimination via Ghost-Enhanced YOLOv8n and EMA Attention under Adverse Condition
---

# EGD-YOLO: A Lightweight Multimodal Framework for Robust Drone-Bird Discrimination via Ghost-Enhanced YOLOv8n and EMA Attention under Adverse Condition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10765" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10765v1</a>
  <a href="https://arxiv.org/pdf/2510.10765.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10765v1" onclick="toggleFavorite(this, '2510.10765v1', 'EGD-YOLO: A Lightweight Multimodal Framework for Robust Drone-Bird Discrimination via Ghost-Enhanced YOLOv8n and EMA Attention under Adverse Condition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sudipto Sarkar, Mohammad Asif Hasan, Khondokar Ashik Shahriar, Fablia Labiba, Nahian Tasnim, Sheikh Anawarul Haq Fattah

**分类**: cs.CV

**发布日期**: 2025-10-12

---

## 💡 一句话要点

**EGD-YOLO：轻量级多模态框架，通过Ghost增强YOLOv8n和EMA注意力实现恶劣条件下无人机-鸟类稳健区分**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机检测` `鸟类检测` `多模态融合` `目标检测` `轻量化模型` `注意力机制` `YOLOv8` `红外图像`

## 📋 核心要点

1. 现有方法在复杂环境下的无人机和鸟类区分精度不足，且计算成本较高，难以满足实时性需求。
2. EGD-YOLOv8n通过Ghost模块增强特征提取，EMA注意力机制关注关键信息，并设计专用检测头以适应不同尺寸目标。
3. 实验表明，多模态融合的EGD-YOLOv8n在准确性和可靠性方面表现最佳，同时保持了实时性，适用于常见GPU。

## 📝 摘要（中文）

本研究针对天空安全和安防系统改进中无人机与鸟类正确识别的关键需求，提出了EGD-YOLOv8n，一种轻量级但功能强大的目标检测模型。该模型利用VIP CUP 2025数据集提供的RGB和红外(IR)图像，改进了图像特征的捕获和理解方式，从而提高了检测的准确性和效率。通过巧妙的设计变更和注意力层，该模型能够专注于重要细节，同时减少所需的计算量。一个特殊的检测头帮助模型适应不同形状和大小的目标。研究训练了三个版本：一个使用RGB图像，一个使用IR图像，一个结合使用两者。组合模型在常见GPU上实现了最佳的准确性和可靠性，同时保持了足够的实时运行速度。

## 🔬 方法详解

**问题定义**：论文旨在解决在复杂和恶劣条件下，准确且高效地区分无人机和鸟类的问题。现有方法通常面临光照变化、背景干扰等挑战，导致检测精度下降，同时计算复杂度较高，难以满足实时应用的需求。

**核心思路**：论文的核心思路是设计一个轻量级但功能强大的多模态目标检测框架，通过结合RGB和红外图像的信息，利用Ghost模块增强特征提取，并引入EMA注意力机制关注关键特征，从而提高检测的准确性和鲁棒性。

**技术框架**：EGD-YOLOv8n框架基于YOLOv8n，主要包含以下模块：1) 输入层：接收RGB和红外图像；2) Ghost模块：用于增强特征提取，减少计算量；3) EMA注意力机制：关注图像中的关键区域；4) 特殊检测头：用于适应不同大小和形状的目标；5) 输出层：输出目标检测结果。训练过程中，分别训练RGB、IR以及RGB-IR融合模型。

**关键创新**：论文的关键创新在于：1) 提出了EGD-YOLOv8n，一种轻量级但功能强大的目标检测模型；2) 结合RGB和红外图像进行多模态融合，提高了检测的鲁棒性；3) 引入Ghost模块和EMA注意力机制，在保证精度的前提下，降低了计算复杂度。

**关键设计**：论文的关键设计包括：1) Ghost模块的具体结构和参数设置，用于生成更多的特征图，同时减少计算量；2) EMA注意力机制的实现细节，用于关注图像中的关键区域；3) 特殊检测头的结构设计，用于适应不同大小和形状的目标；4) 损失函数的选择和优化策略，用于提高模型的训练效果。

## 📊 实验亮点

该研究提出的EGD-YOLOv8n模型在VIP CUP 2025数据集上取得了显著成果。多模态融合模型在准确性和可靠性方面均优于单模态模型，且在常见GPU上实现了实时运行。具体性能数据（如mAP）和与基线模型的对比数据（如YOLOv8n）在论文中进行了详细展示，表明EGD-YOLOv8n在无人机-鸟类区分任务中具有明显的优势。

## 🎯 应用场景

该研究成果可广泛应用于天空安全监控、无人机交通管理、野生动物保护等领域。通过准确区分无人机和鸟类，可以有效预防无人机入侵禁飞区、减少鸟击事件，并为无人机监管提供技术支持。未来，该技术有望集成到智能安防系统中，提升整体安全水平。

## 📄 摘要（原文）

> Identifying drones and birds correctly is essential for keeping the skies safe and improving security systems. Using the VIP CUP 2025 dataset, which provides both RGB and infrared (IR) images, this study presents EGD-YOLOv8n, a new lightweight yet powerful model for object detection. The model improves how image features are captured and understood, making detection more accurate and efficient. It uses smart design changes and attention layers to focus on important details while reducing the amount of computation needed. A special detection head helps the model adapt to objects of different shapes and sizes. We trained three versions: one using RGB images, one using IR images, and one combining both. The combined model achieved the best accuracy and reliability while running fast enough for real-time use on common GPUs.

