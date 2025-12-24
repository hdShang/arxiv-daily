---
layout: default
title: "InfraDiffusion: zero-shot depth map restoration with diffusion models and prompted segmentation from sparse infrastructure point clouds"
---

# InfraDiffusion: zero-shot depth map restoration with diffusion models and prompted segmentation from sparse infrastructure point clouds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03324" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03324v1</a>
  <a href="https://arxiv.org/pdf/2509.03324.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03324v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03324v1', 'InfraDiffusion: zero-shot depth map restoration with diffusion models and prompted segmentation from sparse infrastructure point clouds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixiong Jing, Cheng Zhang, Haibing Wu, Guangming Wang, Olaf Wysocki, Brian Sheil

**分类**: cs.CV

**发布日期**: 2025-09-03

**🔗 代码/项目**: [GITHUB](https://github.com/Jingyixiong/InfraDiffusion-official-implement)

---

## 💡 一句话要点

**InfraDiffusion：利用扩散模型和提示分割实现零样本深度图修复，用于稀疏基础设施点云**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `深度图修复` `扩散模型` `点云处理` `零样本学习` `基础设施检测` `语义分割` `砌体结构`

## 📋 核心要点

1. 现有方法难以从光照不足环境中获取高质量图像，而点云虽然对光照不敏感，但其稀疏性和噪声限制了精细分割。
2. InfraDiffusion通过虚拟相机将点云投影为深度图，并利用改进的DDNM模型进行修复，无需特定任务训练。
3. 实验表明，该方法显著提升了深度图的视觉质量和几何一致性，并改善了基于SAM的砖块级分割性能。

## 📝 摘要（中文）

本文提出了一种名为InfraDiffusion的零样本框架，用于修复稀疏基础设施点云生成的深度图。该框架利用虚拟相机将砌体点云投影为深度图，并通过改进的去噪扩散零空间模型（DDNM）进行修复。InfraDiffusion无需特定任务的训练，即可增强深度图的视觉清晰度和几何一致性。在砌体桥梁和隧道点云数据集上的实验表明，使用Segment Anything Model（SAM）进行砖块级分割时，性能得到显著提升，突显了该方法在砌体结构自动化检测方面的潜力。代码和数据已在https://github.com/Jingyixiong/InfraDiffusion-official-implement上公开。

## 🔬 方法详解

**问题定义**：论文旨在解决从稀疏、非结构化和噪声大的基础设施点云中恢复高质量深度图的问题，特别是针对砌体结构（如桥梁和隧道）的砖块级分割。现有方法在低光照环境下难以获取高质量RGB图像，而直接使用原始点云进行精细分割面临点云稀疏性和噪声的挑战。

**核心思路**：论文的核心思路是将点云投影为深度图，然后利用扩散模型进行图像修复，从而提高深度图的视觉清晰度和几何一致性。这种方法利用了扩散模型强大的生成能力，可以在没有特定任务训练的情况下，有效地填充点云中的缺失信息和去除噪声。

**技术框架**：InfraDiffusion框架主要包含两个阶段：1) 点云到深度图的投影：使用虚拟相机将三维点云投影为二维深度图。虚拟相机的参数（如位置、方向、视场角）需要根据点云的几何特性进行设置。2) 深度图修复：使用改进的去噪扩散零空间模型（DDNM）对深度图进行修复。DDNM是一种基于扩散模型的图像修复方法，它通过迭代地添加噪声和去噪来生成高质量的修复结果。

**关键创新**：该论文的关键创新在于将扩散模型应用于基础设施点云生成的深度图修复任务，并提出了一个零样本的框架。与传统的图像修复方法相比，扩散模型能够更好地处理深度图中的复杂结构和纹理，并且无需针对特定类型的砌体结构进行训练。此外，该方法还结合了Segment Anything Model (SAM) 进行下游的砖块级分割，验证了修复后的深度图的有效性。

**关键设计**：论文中使用了Denoising Diffusion Null-space Model (DDNM) 作为深度图修复的核心。DDNM的关键在于利用扩散过程的零空间来约束修复结果，从而保证修复结果的几何一致性。具体的参数设置和网络结构细节在论文中可能有所描述，但摘要中未明确指出。虚拟相机的参数设置，例如相机的位置和方向，对深度图的质量有重要影响，需要根据具体的点云数据进行调整。

## 📊 实验亮点

该研究在砌体桥梁和隧道点云数据集上进行了实验，结果表明，使用InfraDiffusion修复后的深度图，能够显著提升基于Segment Anything Model（SAM）的砖块级分割性能。具体提升幅度未在摘要中给出，但强调了该方法在自动化检测砌体结构方面的潜力。

## 🎯 应用场景

InfraDiffusion可应用于基础设施的自动化检测和维护，例如桥梁、隧道、建筑物等。通过提高深度图的质量，可以更准确地识别结构中的缺陷（如裂缝、剥落、腐蚀），从而帮助工程师及时发现问题并进行修复，延长基础设施的使用寿命，降低维护成本，并提高安全性。该方法在光照条件差或难以获取高质量图像的场景下具有显著优势。

## 📄 摘要（原文）

> Point clouds are widely used for infrastructure monitoring by providing geometric information, where segmentation is required for downstream tasks such as defect detection. Existing research has automated semantic segmentation of structural components, while brick-level segmentation (identifying defects such as spalling and mortar loss) has been primarily conducted from RGB images. However, acquiring high-resolution images is impractical in low-light environments like masonry tunnels. Point clouds, though robust to dim lighting, are typically unstructured, sparse, and noisy, limiting fine-grained segmentation. We present InfraDiffusion, a zero-shot framework that projects masonry point clouds into depth maps using virtual cameras and restores them by adapting the Denoising Diffusion Null-space Model (DDNM). Without task-specific training, InfraDiffusion enhances visual clarity and geometric consistency of depth maps. Experiments on masonry bridge and tunnel point cloud datasets show significant improvements in brick-level segmentation using the Segment Anything Model (SAM), underscoring its potential for automated inspection of masonry assets. Our code and data is available at https://github.com/Jingyixiong/InfraDiffusion-official-implement.

