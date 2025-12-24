---
layout: default
title: "Follow-Your-Motion: Video Motion Transfer via Efficient Spatial-Temporal Decoupled Finetuning"
---

# Follow-Your-Motion: Video Motion Transfer via Efficient Spatial-Temporal Decoupled Finetuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05207" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05207v2</a>
  <a href="https://arxiv.org/pdf/2506.05207.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05207v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05207v2', 'Follow-Your-Motion: Video Motion Transfer via Efficient Spatial-Temporal Decoupled Finetuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Ma, Yulong Liu, Qiyuan Zhu, Ayden Yang, Kunyu Feng, Xinhua Zhang, Zhifeng Li, Sirui Han, Chenyang Qi, Qifeng Chen

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-08-13)

**备注**: project page: https://follow-your-motion.github.io/

---

## 💡 一句话要点

**提出Follow-Your-Motion以解决视频运动转移中的不一致性问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `视频运动转移` `低秩适应` `空间-时间解耦` `视频扩散变换器` `运动一致性` `稀疏运动采样` `自适应RoPE` `MotionBench`

## 📋 核心要点

1. 现有的运动转移方法在生成视频时存在运动不一致性和微调效率低的问题，尤其是在大型视频扩散变换器上应用时。
2. 本文提出Follow-Your-Motion框架，通过空间-时间解耦的LoRA设计来提高运动转移的效果和效率。
3. 在MotionBench基准上进行的广泛评估显示，Follow-Your-Motion在运动转移任务中表现出显著的优势。

## 📝 摘要（中文）

近年来，视频扩散变换器在多样化运动生成方面取得了显著突破。针对运动转移任务，现有方法主要采用两阶段的低秩适应（LoRA）微调以提高性能。然而，现有的基于适应的运动转移在应用于大型视频扩散变换器时仍然面临运动不一致性和微调效率低下的问题。为了解决这些问题，本文提出了Follow-Your-Motion，一个高效的两阶段视频运动转移框架，旨在微调强大的视频扩散变换器以合成复杂运动。我们提出了一种空间-时间解耦的LoRA，以解耦注意力架构，实现空间外观和时间运动处理的分离。同时，我们设计了稀疏运动采样和自适应RoPE，以加速微调速度。为填补该领域的基准缺失，我们引入了MotionBench，一个涵盖多样化运动的综合基准。

## 🔬 方法详解

**问题定义**：本文旨在解决现有运动转移方法在生成视频时的运动不一致性和微调效率低下的问题，尤其是在大型视频扩散变换器上应用时，传统的两阶段LoRA微调难以保持生成视频与输入视频之间的运动一致性。

**核心思路**：我们提出Follow-Your-Motion框架，通过引入空间-时间解耦的LoRA设计，分离空间外观和时间运动处理，从而提高运动转移的效果和效率。

**技术框架**：该框架分为两个主要阶段：第一阶段进行初步的LoRA微调以适应视频扩散变换器，第二阶段则采用稀疏运动采样和自适应RoPE加速微调过程。

**关键创新**：最重要的创新点在于空间-时间解耦的LoRA设计，使得注意力机制能够独立处理空间和时间信息，从而有效解决了运动不一致性的问题。

**关键设计**：在设计中，我们采用了稀疏运动采样策略，以减少计算量，并通过自适应RoPE来加速微调速度，确保在保持性能的同时提高效率。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

在MotionBench基准上，Follow-Your-Motion框架在运动转移任务中表现出显著的性能提升，相较于传统的LoRA微调方法，运动一致性提高了XX%，微调速度提升了YY%，验证了其在复杂运动合成中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括电影制作、游戏开发和虚拟现实等，能够为这些领域提供高效的运动转移技术，提升视频内容生成的质量和效率。未来，该技术可能推动更多创意应用的发展，改变视频制作的方式。

## 📄 摘要（原文）

> Recently, breakthroughs in the video diffusion transformer have shown remarkable capabilities in diverse motion generations. As for the motion-transfer task, current methods mainly use two-stage Low-Rank Adaptations (LoRAs) finetuning to obtain better performance. However, existing adaptation-based motion transfer still suffers from motion inconsistency and tuning inefficiency when applied to large video diffusion transformers. Naive two-stage LoRA tuning struggles to maintain motion consistency between generated and input videos due to the inherent spatial-temporal coupling in the 3D attention operator. Additionally, they require time-consuming fine-tuning processes in both stages. To tackle these issues, we propose Follow-Your-Motion, an efficient two-stage video motion transfer framework that finetunes a powerful video diffusion transformer to synthesize complex motion. Specifically, we propose a spatial-temporal decoupled LoRA to decouple the attention architecture for spatial appearance and temporal motion processing. During the second training stage, we design the sparse motion sampling and adaptive RoPE to accelerate the tuning speed. To address the lack of a benchmark for this field, we introduce MotionBench, a comprehensive benchmark comprising diverse motion, including creative camera motion, single object motion, multiple object motion, and complex human motion. We show extensive evaluations on MotionBench to verify the superiority of Follow-Your-Motion.

