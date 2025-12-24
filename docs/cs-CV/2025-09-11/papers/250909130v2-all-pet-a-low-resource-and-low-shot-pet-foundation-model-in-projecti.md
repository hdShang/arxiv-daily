---
layout: default
title: "ALL-PET: A Low-resource and Low-shot PET Foundation Model in Projection Domain"
---

# ALL-PET: A Low-resource and Low-shot PET Foundation Model in Projection Domain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09130" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09130v2</a>
  <a href="https://arxiv.org/pdf/2509.09130.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09130v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09130v2', 'ALL-PET: A Low-resource and Low-shot PET Foundation Model in Projection Domain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bin Huang, Kang Chen, Bingxuan Li, Huafeng Liu, Qiegen Liu

**分类**: cs.CV

**发布日期**: 2025-09-11 (更新: 2025-09-16)

---

## 💡 一句话要点

**ALL-PET：一种低资源、低样本的投影域PET基础模型**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `PET成像` `基础模型` `低资源学习` `潜在扩散模型` `正弦图` `数据增强` `医学影像` `几何约束`

## 📋 核心要点

1. 现有PET成像基础模型受限于标注数据稀缺和计算资源不足，难以有效构建。
2. ALL-PET通过在投影域利用潜在扩散模型，结合Radon掩码增强等策略，实现低资源下的高性能。
3. 实验表明，ALL-PET仅需少量样本即可生成高质量正弦图，并在多种PET成像任务中表现出色。

## 📝 摘要（中文）

构建大规模PET成像基础模型面临着标注数据有限和计算资源不足的挑战。为了克服数据稀缺和效率限制，我们提出了ALL-PET，一种直接在投影域操作的低资源、低样本PET基础模型。ALL-PET利用潜在扩散模型（LDM），并具有三个关键创新。首先，我们设计了一种Radon掩码增强策略（RMAS），通过将随机图像域掩码投影到正弦图空间，生成超过20万个结构多样的训练样本，从而以最少的数据显著提高泛化能力。这通过动态多掩码（DMM）机制进行扩展，该机制改变掩码数量和分布，在不增加模型复杂性的情况下增强数据多样性。其次，我们实施正/负掩码约束以嵌入严格的几何一致性，减少参数负担，同时保持生成质量。第三，我们引入透明医学注意力（TMA），一种无参数、几何驱动的机制，增强原始投影数据中与病灶相关的区域。病灶聚焦的注意力图从粗分割中导出，覆盖高代谢和低代谢区域，并投影到正弦图空间以实现物理一致的指导。该系统支持临床医生定义的ROI调整，确保与PET采集物理对齐的灵活、可解释和任务自适应的强调。实验结果表明，ALL-PET仅使用500个样本即可实现高质量的正弦图生成，其性能与在更大的数据集上训练的模型相当。ALL-PET可推广到包括低剂量重建、衰减校正、延迟帧预测和示踪剂分离等任务，并在低于24GB的内存使用情况下高效运行。

## 🔬 方法详解

**问题定义**：PET成像基础模型的构建面临数据量不足和计算资源有限的双重挑战。现有方法通常需要大量的标注数据进行训练，且计算成本高昂，限制了其在实际临床应用中的推广。

**核心思路**：ALL-PET的核心思路是在投影域（正弦图空间）直接进行模型训练，并利用数据增强和几何约束来克服数据稀缺的问题。通过在正弦图空间进行操作，可以更好地利用PET成像的物理特性，并减少对大量图像域标注数据的依赖。

**技术框架**：ALL-PET基于潜在扩散模型（LDM），主要包含以下几个模块：1) Radon掩码增强策略（RMAS）和动态多掩码（DMM）用于生成大量结构多样的训练样本；2) 正/负掩码约束用于嵌入几何一致性；3) 透明医学注意力（TMA）机制用于增强病灶相关区域的关注。整体流程为：首先利用RMAS和DMM进行数据增强，然后将增强后的数据输入到LDM中进行训练，同时施加正/负掩码约束，最后利用TMA机制引导模型关注病灶区域。

**关键创新**：ALL-PET的关键创新在于：1) 提出了一种新的数据增强方法，即Radon掩码增强策略（RMAS），可以在数据量极少的情况下生成大量结构多样的训练样本；2) 引入了透明医学注意力（TMA）机制，可以在不增加模型参数的情况下，引导模型关注病灶区域，提高生成质量；3) 通过正/负掩码约束，嵌入了严格的几何一致性，减少了参数负担。

**关键设计**：RMAS通过将随机图像域掩码投影到正弦图空间来生成训练样本。DMM动态调整掩码的数量和分布，以增加数据多样性。正/负掩码约束通过限制生成结果中正负像素的分布来保证几何一致性。TMA利用粗分割结果生成注意力图，并将其投影到正弦图空间，以引导模型关注病灶区域。TMA是无参数的，并且支持临床医生定义的ROI调整。

## 📊 实验亮点

ALL-PET仅使用500个样本即可实现高质量的正弦图生成，其性能与在更大的数据集上训练的模型相当。该模型在低剂量重建、衰减校正、延迟帧预测和示踪剂分离等任务中均表现出良好的泛化能力，且内存占用低于24GB，具有很高的实用价值。

## 🎯 应用场景

ALL-PET在PET成像领域具有广泛的应用前景，包括低剂量PET重建、衰减校正、动态PET成像的延迟帧预测以及PET示踪剂分离等。该模型能够降低对大量标注数据的依赖，减少计算资源需求，加速PET成像技术的临床转化，并有望提升疾病诊断的准确性和效率。

## 📄 摘要（原文）

> Building large-scale foundation model for PET imaging is hindered by limited access to labeled data and insufficient computational resources. To overcome data scarcity and efficiency limitations, we propose ALL-PET, a low-resource, low-shot PET foundation model operating directly in projection domain. ALL-PET leverages a latent diffusion model (LDM) with three key innovations. First, we design a Radon mask augmentation strategy (RMAS) that generates over 200,000 structurally diverse training samples by projecting randomized image-domain masks into sinogram space, significantly improving generalization with minimal data. This is extended by a dynamic multi-mask (DMM) mechanism that varies mask quantity and distribution, enhancing data diversity without added model complexity. Second, we implement positive/negative mask constraints to embed strict geometric consistency, reducing parameter burden while preserving generation quality. Third, we introduce transparent medical attention (TMA), a parameter-free, geometry-driven mechanism that enhances lesion-related regions in raw projection data. Lesion-focused attention maps are derived from coarse segmentation, covering both hypermetabolic and hypometabolic areas, and projected into sinogram space for physically consistent guidance. The system supports clinician-defined ROI adjustments, ensuring flexible, interpretable, and task-adaptive emphasis aligned with PET acquisition physics. Experimental results show that ALL-PET achieves high-quality sinogram generation using only 500 samples, with performance comparable to models trained on larger datasets. ALL-PET generalizes across tasks including low-dose reconstruction, attenuation correction, delayed-frame prediction, and tracer separation, operating efficiently with memory use under 24GB.

