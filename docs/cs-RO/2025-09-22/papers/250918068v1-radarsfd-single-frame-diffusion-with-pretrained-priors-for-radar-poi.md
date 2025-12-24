---
layout: default
title: "RadarSFD: Single-Frame Diffusion with Pretrained Priors for Radar Point Clouds"
---

# RadarSFD: Single-Frame Diffusion with Pretrained Priors for Radar Point Clouds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18068" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18068v1</a>
  <a href="https://arxiv.org/pdf/2509.18068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18068v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18068v1', 'RadarSFD: Single-Frame Diffusion with Pretrained Priors for Radar Point Clouds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bin Zhao, Nakul Garg

**分类**: cs.RO, eess.SP

**发布日期**: 2025-09-22

---

## 💡 一句话要点

**RadarSFD：基于单帧雷达点云和预训练先验的扩散模型**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `雷达点云` `单帧重建` `扩散模型` `预训练先验` `深度估计`

## 📋 核心要点

1. 现有雷达成像方法依赖合成孔径或多帧聚合来提高分辨率，这对于小型无人机或可穿戴系统不切实际。
2. RadarSFD利用预训练的单目深度估计器先验，通过条件扩散模型从单帧雷达数据重建稠密点云。
3. 实验表明，RadarSFD在RadarHD数据集上优于单帧基线，并与多帧方法具有竞争力，同时具备良好的泛化能力。

## 📝 摘要（中文）

本文提出了一种名为RadarSFD的条件潜在扩散框架，用于从单帧雷达数据重建稠密的、类似激光雷达的点云，无需运动或合成孔径雷达（SAR）。该方法将预训练的单目深度估计器的几何先验知识迁移到扩散模型的骨干网络中，并通过通道级的潜在空间拼接将这些先验与雷达输入对齐。此外，还采用了一种结合潜在空间和像素空间损失的双空间目标函数来正则化输出。在RadarHD基准测试中，RadarSFD实现了35厘米的Chamfer距离和28厘米的修正Hausdorff距离，优于单帧RadarHD基线（56厘米，45厘米），并与使用5-41帧的多帧方法相比具有竞争力。定性结果表明，该方法能够恢复精细的墙壁和狭窄的间隙，并且在新的环境中进行的实验证实了其强大的泛化能力。消融研究突出了预训练初始化、雷达BEV条件化和双空间损失的重要性。这些结果共同确立了第一个实用的单帧、无SAR毫米波雷达管道，用于紧凑型机器人系统中的稠密点云感知。

## 🔬 方法详解

**问题定义**：论文旨在解决在资源受限的机器人平台上，如何仅使用单帧毫米波雷达数据生成高分辨率、稠密点云的问题。现有方法依赖于多帧数据或合成孔径雷达技术，这在小型化、低功耗的机器人应用中是不现实的，限制了雷达在这些场景下的应用。

**核心思路**：RadarSFD的核心思路是利用预训练的单目深度估计器学习到的几何先验知识，将其融入到扩散模型中，从而指导单帧雷达数据的点云重建过程。通过将雷达数据与深度先验信息相结合，可以有效地弥补单帧雷达数据的信息缺失，生成更准确、更稠密的点云。

**技术框架**：RadarSFD采用条件潜在扩散模型框架。整体流程包括：1）使用预训练的单目深度估计器提取几何先验；2）将雷达鸟瞰图（BEV）特征与深度先验特征在潜在空间进行通道级联接，作为扩散模型的条件输入；3）通过扩散模型的迭代去噪过程，生成最终的稠密点云。该框架利用了扩散模型强大的生成能力和预训练模型的先验知识。

**关键创新**：RadarSFD的关键创新在于：1）将预训练的单目深度估计器作为几何先验引入雷达点云重建任务，有效利用了视觉领域的知识；2）提出了通道级的潜在空间拼接方法，将雷达数据与深度先验信息有效融合；3）设计了双空间损失函数，同时在潜在空间和像素空间进行约束，提高了重建质量。

**关键设计**：RadarSFD的关键设计包括：1）使用ResNet作为单目深度估计器的骨干网络；2）采用U-Net结构的扩散模型，并使用DDPM作为采样策略；3）双空间损失函数由潜在空间L1损失和像素空间Chamfer距离损失组成，平衡了重建的准确性和稠密度。雷达BEV图作为条件输入，引导扩散过程。

## 📊 实验亮点

RadarSFD在RadarHD数据集上取得了显著的性能提升。与单帧RadarHD基线相比，Chamfer距离从56厘米降低到35厘米，修正Hausdorff距离从45厘米降低到28厘米。此外，RadarSFD的性能与使用5-41帧的多帧方法相比具有竞争力，证明了其在单帧雷达数据处理方面的优势。

## 🎯 应用场景

RadarSFD在小型机器人平台，如无人机、检查机器人和可穿戴设备上具有广泛的应用前景。它可以为这些平台提供鲁棒的感知能力，尤其是在光照条件差或存在烟雾、灰尘等恶劣环境的情况下。该技术可以用于自主导航、环境建模、目标检测和避障等任务，提高机器人的自主性和适应性。

## 📄 摘要（原文）

> Millimeter-wave radar provides perception robust to fog, smoke, dust, and low light, making it attractive for size, weight, and power constrained robotic platforms. Current radar imaging methods, however, rely on synthetic aperture or multi-frame aggregation to improve resolution, which is impractical for small aerial, inspection, or wearable systems. We present RadarSFD, a conditional latent diffusion framework that reconstructs dense LiDAR-like point clouds from a single radar frame without motion or SAR. Our approach transfers geometric priors from a pretrained monocular depth estimator into the diffusion backbone, anchors them to radar inputs via channel-wise latent concatenation, and regularizes outputs with a dual-space objective combining latent and pixel-space losses. On the RadarHD benchmark, RadarSFD achieves 35 cm Chamfer Distance and 28 cm Modified Hausdorff Distance, improving over the single-frame RadarHD baseline (56 cm, 45 cm) and remaining competitive with multi-frame methods using 5-41 frames. Qualitative results show recovery of fine walls and narrow gaps, and experiments across new environments confirm strong generalization. Ablation studies highlight the importance of pretrained initialization, radar BEV conditioning, and the dual-space loss. Together, these results establish the first practical single-frame, no-SAR mmWave radar pipeline for dense point cloud perception in compact robotic systems.

