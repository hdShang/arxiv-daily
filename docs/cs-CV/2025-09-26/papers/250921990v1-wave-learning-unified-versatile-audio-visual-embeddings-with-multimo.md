---
layout: default
title: "WAVE: Learning Unified & Versatile Audio-Visual Embeddings with Multimodal LLM"
---

# WAVE: Learning Unified & Versatile Audio-Visual Embeddings with Multimodal LLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21990" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21990v1</a>
  <a href="https://arxiv.org/pdf/2509.21990.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21990v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21990v1', 'WAVE: Learning Unified & Versatile Audio-Visual Embeddings with Multimodal LLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changli Tang, Qinfan Xiao, Ke Mei, Tianyi Wang, Fengyun Rao, Chao Zhang

**分类**: cs.CV, cs.SD

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**WAVE：利用多模态LLM学习统一且通用的音视频嵌入**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `音视频嵌入` `大型语言模型` `跨模态检索` `提示学习`

## 📋 核心要点

1. 多模态LLM嵌入在通用表示方面表现出色，但在音频和视频等动态模态中的应用仍有待探索。
2. WAVE通过分层特征融合和联合多模态多任务训练，为文本、音频和视频创建统一的嵌入空间。
3. 实验表明，WAVE在跨模态检索和多模态问答方面均优于现有模型，并在MMEB-v2上取得SOTA。

## 📝 摘要（中文）

本文提出WAVE（统一且通用的音视频嵌入），这是一种基于LLM的嵌入方法，旨在为文本、音频和视频模态创建统一的表示空间。WAVE采用了一种新颖的分层特征融合策略和联合多模态、多任务训练方法，从而实现两个关键能力：任意到任意的跨模态检索，以及生成针对用户指令定制的提示感知嵌入。实验表明，WAVE在MMEB-v2视频基准测试中取得了新的state-of-the-art，并在音频和视频到音频的检索中取得了优异的结果。其提示感知特性在多模态问答中也表现出色，显著优于现有的嵌入模型。消融研究验证了联合训练策略，证明了所有模态的性能均有所提高。WAVE引入了一个用于通用音视频学习的新基准，为跨模态、任意到任意的应用开辟了广阔的可能性。代码、检查点和数据将会开源。

## 🔬 方法详解

**问题定义**：现有方法在处理音视频等多模态数据时，缺乏一个统一的表示空间，导致跨模态检索和理解能力受限。特别是，如何利用大型语言模型（LLM）的强大能力来提升音视频嵌入的通用性和灵活性是一个挑战。

**核心思路**：WAVE的核心思路是利用多模态LLM构建一个统一的嵌入空间，使得文本、音频和视频可以被映射到同一空间中进行比较和推理。通过联合多模态、多任务训练，模型可以学习到跨模态的关联性，并具备根据用户指令生成定制化嵌入的能力。

**技术框架**：WAVE的技术框架主要包括三个部分：首先，对不同模态的数据（文本、音频、视频）进行特征提取；然后，采用分层特征融合策略，将不同模态的特征进行融合；最后，通过联合多模态、多任务训练，优化嵌入空间，使其具备跨模态检索和提示感知能力。

**关键创新**：WAVE的关键创新在于：1）提出了一个基于LLM的统一音视频嵌入框架，能够处理多种模态的数据；2）设计了一种分层特征融合策略，有效地融合了不同模态的特征；3）采用了联合多模态、多任务训练方法，提升了模型的泛化能力和提示感知能力。

**关键设计**：在分层特征融合方面，WAVE可能采用了注意力机制或者其他加权融合方法，以突出不同模态特征的重要性。在损失函数方面，可能采用了对比学习损失或者其他能够拉近相似样本距离、推远不相似样本距离的损失函数。具体的网络结构细节和参数设置需要在论文的详细描述中查找。

## 📊 实验亮点

WAVE在MMEB-v2视频基准测试中取得了新的state-of-the-art，证明了其在视频理解方面的卓越性能。此外，WAVE在音频和视频到音频的检索任务中也取得了优异的结果，表明其跨模态检索能力得到了显著提升。在多模态问答任务中，WAVE显著优于现有的嵌入模型，体现了其提示感知能力的优势。

## 🎯 应用场景

WAVE具有广泛的应用前景，包括跨模态信息检索、视频内容理解、智能客服、多模态对话系统等。例如，用户可以通过语音或文本查询视频内容，或者根据视频内容生成相关的文本描述。该研究有助于提升人机交互的智能化水平，并为多模态数据的应用提供新的思路。

## 📄 摘要（原文）

> While embeddings from multimodal large language models (LLMs) excel as general-purpose representations, their application to dynamic modalities like audio and video remains underexplored. We introduce WAVE (\textbf{u}nified \& \textbf{v}ersatile \textbf{a}udio-\textbf{v}isual \textbf{e}mbeddings), the first LLM-based embedding that creates a unified representation space for text, audio, and video modalities. WAVE employs a novel hierarchical feature fusion strategy and a joint multi-modal, multi-task training approach to enable two key capabilities: any-to-any cross-modal retrieval and the generation of prompt-aware embeddings tailored to user instructions. Experimentally, WAVE sets a new state-of-the-art on the MMEB-v2 video benchmark and achieves superior results in audio and video-to-audio retrieval. Its prompt-aware nature also yields remarkable performance in multimodal question answering, significantly outperforming existing embedding models. Ablation studies validate our joint training strategy, demonstrating improved performance across all modalities. With a newly introduced benchmark for versatile audio-visual learning, WAVE opens up broad possibilities for cross-modal, any-to-any applications. Our code, checkpoints, and data will be released.

