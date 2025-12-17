---
layout: default
title: $\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
---

# $\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21542" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21542v1</a>
  <a href="https://arxiv.org/pdf/2511.21542.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21542v1" onclick="toggleFavorite(this, '2511.21542v1', '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihao Zhan, Jiaying Zhou, Likui Zhang, Qinhan Lv, Hao Liu, Jusheng Zhang, Weizheng Li, Ziliang Chen, Tianshui Chen, Keze Wang, Liang Lin, Guangrun Wang

**分类**: cs.RO, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-11-26

---

## 💡 一句话要点

**提出E0框架，通过连续离散扩散提升VLA模型在机器人操作中的泛化性和精细控制能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉语言动作模型` `机器人操作` `离散扩散` `动作生成` `泛化能力`

## 📋 核心要点

1. 现有VLA模型在泛化性和动作控制精度方面存在不足，难以适应复杂多变的任务环境。
2. E0框架采用连续离散扩散方法，将动作生成视为量化动作token的迭代去噪过程，更好地匹配机器人控制的离散本质。
3. 实验表明，E0在多个基准测试中取得了SOTA性能，并在真实机器人操作中展现出精确、鲁棒和可迁移的控制能力。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型通过整合视觉感知、语言理解和控制生成，为机器人操作提供了一个统一的框架。然而，现有的VLA模型在跨不同任务、场景和相机视角时的泛化能力仍然不足，并且常常产生粗糙或不稳定的动作。我们提出了E0，一个连续离散扩散框架，它将动作生成建模为量化动作token上的迭代去噪过程。与连续扩散策略相比，E0具有两个关键优势：(1)离散动作token与预训练VLM/VLA骨干网络的符号结构自然对齐，从而实现更强的语义条件作用；(2)离散扩散匹配了真实世界机器人控制的量化本质——其硬件约束(例如，编码器分辨率、控制频率、驱动延迟)固有地离散化了连续信号——因此受益于建模正确离散动作分布的贝叶斯最优去噪器，从而带来更强的泛化能力。与离散自回归和基于掩码的离散扩散模型相比，E0支持更大且更细粒度的动作词汇表，并避免了由基于掩码的损坏引入的分布不匹配，从而产生更准确的细粒度动作控制。我们进一步引入了一种球面视点扰动增强方法，以提高对相机移动的鲁棒性，而无需额外数据。在LIBERO、VLABench和ManiSkill上的实验表明，E0在14个不同的环境中实现了最先进的性能，平均优于强大的基线10.7%。在Franka机械臂上的真实世界评估证实，E0提供了精确、鲁棒和可转移的操作，确立了离散扩散作为通用VLA策略学习的一个有希望的方向。

## 🔬 方法详解

**问题定义**：现有VLA模型难以在不同任务、场景和相机视角下泛化，动作控制精度不足，导致机器人操作不稳定。连续动作空间难以与预训练的VLM/VLA骨干网络对齐，且忽略了真实机器人控制的离散本质，而离散动作空间方法又存在词汇表大小限制和分布不匹配问题。

**核心思路**：E0的核心思路是将动作生成建模为离散空间上的扩散过程，通过迭代去噪的方式生成量化的动作token。这种方法既能利用预训练模型的语义信息，又能更好地匹配真实机器人控制的离散特性，从而提高泛化能力和控制精度。同时，通过连续化离散扩散过程，可以支持更大的动作词汇表，避免分布不匹配问题。

**技术框架**：E0框架主要包含以下几个模块：1) 视觉和语言编码器：用于提取视觉和语言特征；2) 离散扩散模型：用于生成量化的动作token，该模型基于Transformer架构，通过迭代去噪的方式生成动作序列；3) 动作解码器：将离散的动作token解码为机器人控制指令。整体流程是：首先，将视觉和语言输入编码为特征向量，然后将这些特征向量作为条件输入到离散扩散模型中，生成一系列离散的动作token，最后将这些token解码为机器人控制指令。

**关键创新**：E0的关键创新在于采用了连续离散扩散框架，将动作生成建模为量化动作token上的迭代去噪过程。与传统的连续扩散策略相比，E0更好地匹配了真实机器人控制的离散本质，并能与预训练VLM/VLA骨干网络的符号结构自然对齐，从而实现更强的语义条件作用。此外，E0还引入了一种球面视点扰动增强方法，以提高对相机移动的鲁棒性。

**关键设计**：E0的关键设计包括：1) 动作token的量化方式：采用k-means聚类等方法将连续动作空间量化为离散的动作token；2) 扩散模型的噪声 schedule：采用线性或余弦噪声schedule，控制噪声的添加过程；3) 损失函数：采用交叉熵损失函数，用于训练扩散模型；4) 网络结构：扩散模型采用Transformer架构，并引入注意力机制，以更好地捕捉动作序列之间的依赖关系。

## 📊 实验亮点

E0在LIBERO、VLABench和ManiSkill等14个不同的环境中实现了最先进的性能，平均优于强大的基线10.7%。在Franka机械臂上的真实世界评估证实，E0能够实现精确、鲁棒和可转移的操作。这些实验结果表明，离散扩散是通用VLA策略学习的一个有希望的方向。

## 🎯 应用场景

E0框架具有广泛的应用前景，可应用于各种机器人操作任务，例如物体抓取、装配、导航等。该研究成果有助于提升机器人在复杂环境中的自主操作能力，降低对人工干预的依赖，从而在工业自动化、智能家居、医疗健康等领域发挥重要作用。未来，E0框架有望进一步扩展到更多模态的输入，例如触觉、力觉等，从而实现更智能、更灵活的机器人控制。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models offer a unified framework for robotic manipulation by integrating visual perception, language understanding, and control generation. Yet existing VLA models still struggle to generalize across diverse tasks, scenes, and camera viewpoints, and often produce coarse or unstable actions. We introduce E0, a continuized discrete diffusion framework that formulates action generation as iterative denoising over quantized action tokens. Compared with continuous diffusion policies, E0 offers two key advantages: (1) discrete action tokens align naturally with the symbolic structure of pretrained VLM/VLA backbones, enabling stronger semantic conditioning; and 2. discrete diffusion matches the true quantized nature of real-world robot control-whose hardware constraints (e.g., encoder resolution, control frequency, actuation latency) inherently discretize continuous signals-and therefore benefits from a Bayes-optimal denoiser that models the correct discrete action distribution, leading to stronger generalization. Compared with discrete autoregressive and mask-based discrete diffusion models, E0 supports a significantly larger and finer-grained action vocabulary and avoids the distributional mismatch introduced by masking-based corruptions-yielding more accurate fine-grained action control. We further introduce a spherical viewpoint perturbation augmentation method to improve robustness to camera shifts without additional data. Experiments on LIBERO, VLABench, and ManiSkill show that E0 achieves state-of-the-art performance across 14 diverse environments, outperforming strong baselines by 10.7% on average. Real-world evaluation on a Franka arm confirms that E0 delivers precise, robust, and transferable manipulation, establishing discrete diffusion as a promising direction for generalizable VLA policy learning.

