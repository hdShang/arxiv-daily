---
layout: default
title: "RangeSAM: On the Potential of Visual Foundation Models for Range-View represented LiDAR segmentation"
---

# RangeSAM: On the Potential of Visual Foundation Models for Range-View represented LiDAR segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15886" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15886v3</a>
  <a href="https://arxiv.org/pdf/2509.15886.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15886v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15886v3', 'RangeSAM: On the Potential of Visual Foundation Models for Range-View represented LiDAR segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Paul Julius Kühn, Duc Anh Nguyen, Arjan Kuijper, Holger Graf, Saptarshi Neil Sinha

**分类**: cs.CV

**发布日期**: 2025-09-19 (更新: 2025-11-13)

---

## 💡 一句话要点

**RangeSAM：探索视觉基础模型在激光雷达Range-View分割中的潜力**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `点云分割` `激光雷达` `Range-View` `视觉基础模型` `SAM2` `自动驾驶` `三维场景理解`

## 📋 核心要点

1. 现有点云分割方法计算成本高，内存访问不规则，实时性差，限制了其在自动驾驶等领域的应用。
2. RangeSAM通过将SAM2视觉基础模型适配到Range-View表示，利用高效的2D特征提取进行3D分割。
3. RangeSAM在SemanticKITTI数据集上取得了有竞争力的性能，同时保持了2D方法的快速性和可扩展性。

## 📝 摘要（中文）

点云分割是自动驾驶和三维场景理解的核心。虽然基于体素和点的方法因其与深度架构的兼容性以及捕获细粒度几何信息的能力而在最近的研究中占据主导地位，但它们通常会产生高计算成本、不规则的内存访问和有限的实时效率。相比之下，Range-View方法虽然相对未被充分探索，但可以利用成熟的二维语义分割技术来实现快速而准确的预测。受到视觉基础模型（VFM）在字幕生成、零样本识别和多模态任务方面快速进展的推动，我们研究了SAM2（当前最先进的分割VFM）是否可以作为Range-View表示的激光雷达点云分割的强大骨干网络。我们提出了RangeSAM，据我们所知，这是第一个将SAM2适配到三维分割的Range-View框架，将高效的二维特征提取与标准投影/反投影相结合，以处理点云。为了优化SAM2用于Range-View表示，我们对编码器进行了一些架构修改：（1）一个强调激光雷达Range图像中固有的水平空间依赖性的新模块，（2）一个定制的配置，根据球面投影的几何特性量身定制，以及（3）一个在编码器骨干中专门设计的自适应机制，用于捕获Range-View伪图像中存在的独特空间模式和不连续性。我们的方法在SemanticKITTI上实现了有竞争力的性能，同时受益于二维中心管道的速度、可扩展性和部署简单性。这项工作突出了VFM作为三维感知通用骨干网络的可行性，并开辟了一条通往统一的、基础模型驱动的激光雷达分割的道路。结果让我们得出结论，使用VFM的Range-View分割方法会带来有希望的结果。

## 🔬 方法详解

**问题定义**：论文旨在解决激光雷达点云分割问题，特别是针对现有基于体素和点的方法计算成本高、内存访问不规则以及实时性差的痛点。这些问题限制了它们在资源受限或需要实时响应的应用场景中的部署。

**核心思路**：论文的核心思路是利用视觉基础模型（VFMs）在2D图像分割方面的强大能力，并将其迁移到3D点云分割任务中。具体来说，作者选择了SAM2作为基础模型，并将其适配到Range-View表示的点云数据上。通过将3D点云投影到2D Range图像，可以利用成熟的2D图像处理技术，从而提高分割效率和降低计算成本。

**技术框架**：RangeSAM的整体框架包括以下几个主要步骤：1) 将3D点云数据投影到2D Range图像；2) 使用修改后的SAM2编码器提取Range图像的特征；3) 使用SAM2解码器进行像素级别的分割预测；4) 将2D分割结果反投影回3D点云，得到最终的3D分割结果。其中，SAM2编码器是经过专门优化的，以适应Range图像的特性。

**关键创新**：论文的关键创新在于将视觉基础模型SAM2成功地应用于激光雷达点云分割任务，并针对Range-View表示的特点进行了专门的优化。具体来说，作者提出了以下几个创新点：1) 引入了一个新的模块，用于强调Range图像中固有的水平空间依赖性；2) 对SAM2的配置进行了定制，以适应球面投影的几何特性；3) 在SAM2编码器中设计了一个自适应机制，用于捕获Range图像中存在的独特空间模式和不连续性。

**关键设计**：为了强调水平空间依赖性，作者设计了一个专门的模块，该模块可能包含卷积层或注意力机制，用于捕捉水平方向上的上下文信息。为了适应球面投影的几何特性，作者可能调整了SAM2的感受野大小或采样策略。为了捕捉Range图像中的不连续性，作者可能引入了边缘检测算子或设计了专门的损失函数。

## 📊 实验亮点

RangeSAM在SemanticKITTI数据集上取得了有竞争力的性能，证明了视觉基础模型在激光雷达点云分割中的潜力。该方法受益于2D中心管道的速度、可扩展性和部署简单性，为未来的研究提供了一个新的方向。具体性能数据和对比基线需要在论文中查找。

## 🎯 应用场景

RangeSAM具有广泛的应用前景，包括自动驾驶、机器人导航、三维场景重建等领域。该方法可以用于提高自动驾驶系统的环境感知能力，帮助机器人更好地理解周围环境，以及加速三维场景的重建过程。此外，该方法还可以应用于智慧城市、虚拟现实等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Point cloud segmentation is central to autonomous driving and 3D scene understanding. While voxel- and point-based methods dominate recent research due to their compatibility with deep architectures and ability to capture fine-grained geometry, they often incur high computational cost, irregular memory access, and limited real-time efficiency. In contrast, range-view methods, though relatively underexplored - can leverage mature 2D semantic segmentation techniques for fast and accurate predictions. Motivated by the rapid progress in Visual Foundation Models (VFMs) for captioning, zero-shot recognition, and multimodal tasks, we investigate whether SAM2, the current state-of-the-art VFM for segmentation tasks, can serve as a strong backbone for LiDAR point cloud segmentation in the range view. We present , to our knowledge, the first range-view framework that adapts SAM2 to 3D segmentation, coupling efficient 2D feature extraction with standard projection/back-projection to operate on point clouds. To optimize SAM2 for range-view representations, we implement several architectural modifications to the encoder: (1) a novel module that emphasizes horizontal spatial dependencies inherent in LiDAR range images, (2) a customized configuration of tailored to the geometric properties of spherical projections, and (3) an adapted mechanism in the encoder backbone specifically designed to capture the unique spatial patterns and discontinuities present in range-view pseudo-images. Our approach achieves competitive performance on SemanticKITTI while benefiting from the speed, scalability, and deployment simplicity of 2D-centric pipelines. This work highlights the viability of VFMs as general-purpose backbones for 3D perception and opens a path toward unified, foundation-model-driven LiDAR segmentation. Results lets us conclude that range-view segmentation methods using VFMs leads to promising results.

