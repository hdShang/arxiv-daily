---
layout: default
title: Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback
---

# Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.16888" target="_blank" class="toolbar-btn">arXiv: 2510.16888v3</a>
    <a href="https://arxiv.org/pdf/2510.16888.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16888v3" 
            onclick="toggleFavorite(this, '2510.16888v3', 'Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zongjian Li, Zheyuan Liu, Qihui Zhang, Bin Lin, Feize Wu, Shenghai Yuan, Zhiyuan Yan, Yang Ye, Wangbo Yu, Yuwei Niu, Shaodong Wang, Xinhua Cheng, Li Yuan

**分类**: cs.CV

**发布日期**: 2025-10-19 (更新: 2025-11-04)

---

## 💡 一句话要点

**Uniworld-V2：利用扩散负感知微调和MLLM隐式反馈增强图像编辑能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像编辑` `扩散模型` `策略优化` `多模态大语言模型` `奖励模型` `流匹配` `负感知微调`

## 📋 核心要点

1. 现有指令驱动图像编辑模型易于过拟合标注数据，泛化能力受限，难以探索训练分布之外的编辑。
2. 提出Edit-R1框架，核心是DiffusionNFT和MLLM隐式反馈，前者提升训练效率，后者提供细粒度奖励信号。
3. UniWorld-V2在ImgEdit和GEdit-Bench上达到SOTA，且框架具有模型无关性，可提升多种基础模型性能。

## 📝 摘要（中文）

本文提出Edit-R1，一种基于策略优化的指令驱动图像编辑后训练框架。该框架利用扩散负感知微调(DiffusionNFT)，这是一种与流匹配前向过程一致的无似然策略优化方法，从而可以使用更高阶的采样器和更高效的训练。此外，由于编辑指令和任务的多样性，缺乏通用的奖励模型。为了弥合这一差距，本文采用多模态大型语言模型(MLLM)作为统一的、免训练的奖励模型，利用其输出logits提供细粒度的反馈。此外，精心设计了一种低方差的群体过滤机制，以减少MLLM评分噪声并稳定优化。使用该框架训练的UniWorld-V2在ImgEdit和GEdit-Bench基准测试中取得了最先进的结果，分别获得了4.49和7.83分。重要的是，该框架是模型无关的，当应用于Qwen-Image-Edit和FLUX-Kontext等不同的基础模型时，可提供显著的性能提升，证明了其广泛的适用性。代码和模型已公开。

## 🔬 方法详解

**问题定义**：指令驱动的图像编辑任务旨在根据给定的文本指令修改图像。现有方法主要依赖于监督微调，但容易过拟合训练数据，导致泛化能力不足，无法处理未见过的编辑指令或图像。此外，缺乏有效的奖励机制来指导模型学习，尤其是对于复杂的编辑任务。

**核心思路**：本文的核心思路是利用策略优化方法，通过奖励信号引导模型学习更好的编辑策略。具体而言，采用DiffusionNFT方法进行微调，该方法与扩散模型的训练过程一致，可以更有效地利用预训练的扩散模型。同时，利用MLLM作为奖励模型，无需额外训练即可提供细粒度的反馈信号，从而克服了缺乏通用奖励模型的难题。

**技术框架**：Edit-R1框架主要包含以下几个阶段：1) 使用预训练的扩散模型作为基础模型；2) 使用DiffusionNFT方法对基础模型进行微调，优化编辑策略；3) 使用MLLM作为奖励模型，评估编辑结果的质量，并提供反馈信号；4) 使用低方差的群体过滤机制，减少MLLM评分噪声，稳定优化过程。整个框架是一个后训练过程，可以应用于不同的基础模型。

**关键创新**：本文的关键创新在于：1) 提出了DiffusionNFT方法，该方法与扩散模型的训练过程一致，可以更有效地利用预训练的扩散模型；2) 利用MLLM作为奖励模型，无需额外训练即可提供细粒度的反馈信号；3) 设计了低方差的群体过滤机制，减少MLLM评分噪声，稳定优化过程。与现有方法相比，本文的方法可以更有效地提升模型的泛化能力和编辑质量。

**关键设计**：DiffusionNFT方法基于流匹配理论，通过优化一个策略网络来匹配扩散模型的噪声分布。MLLM奖励模型使用其输出logits作为反馈信号，logits可以提供更细粒度的信息，例如，可以区分不同的编辑属性。群体过滤机制通过对多个编辑结果进行评分，并取平均值来减少MLLM评分噪声。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

UniWorld-V2在ImgEdit和GEdit-Bench基准测试中取得了state-of-the-art的结果，分别获得了4.49和7.83分。该框架具有模型无关性，当应用于Qwen-Image-Edit和FLUX-Kontext等不同的基础模型时，可提供显著的性能提升，证明了其广泛的适用性。实验结果表明，本文提出的方法可以有效地提升模型的泛化能力和编辑质量。

## 🎯 应用场景

该研究成果可广泛应用于图像编辑、内容创作、艺术设计等领域。例如，用户可以通过简单的文本指令快速修改图像，生成个性化的内容。该技术还可以应用于自动化图像处理流程，提高效率和质量。未来，该研究有望推动图像编辑技术的进一步发展，实现更智能、更便捷的图像处理。

## 📄 摘要（原文）

> Instruction-based image editing has achieved remarkable progress; however, models solely trained via supervised fine-tuning often overfit to annotated patterns, hindering their ability to explore and generalize beyond training distributions. To this end, we introduce Edit-R1, a novel post-training framework for instruction-based image editing based on policy optimization. Specifically, we utilize Diffusion Negative-aware Finetuning (DiffusionNFT), a likelihood-free policy optimization method consistent with the flow matching forward process, thereby enabling the use of higher-order samplers and more efficient training. Another key challenge here is the absence of a universal reward model, resulting from the diverse nature of editing instructions and tasks. To bridge this gap, we employ a Multimodal Large Language Model (MLLM) as a unified, training-free reward model, leveraging its output logits to provide fine-grained feedback. Furthermore, we carefully design a low-variance group filtering mechanism to reduce MLLM scoring noise and stabilize optimization. \texttt{UniWorld-V2}, trained with this framework, achieves \textbf{state-of-the-art} results on the ImgEdit and GEdit-Bench benchmarks, scoring 4.49 and 7.83, respectively. Crucially, our framework is model-agnostic, delivering substantial performance gains when applied to diverse base models like Qwen-Image-Edit and FLUX-Kontext, demonstrating its wide applicability. Code and models are publicly available to support further research.

