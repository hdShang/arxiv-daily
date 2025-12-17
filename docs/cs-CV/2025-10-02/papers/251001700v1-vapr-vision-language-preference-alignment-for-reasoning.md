---
layout: default
title: VaPR -- Vision-language Preference alignment for Reasoning
---

# VaPR -- Vision-language Preference alignment for Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01700" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01700v1</a>
  <a href="https://arxiv.org/pdf/2510.01700.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01700v1" onclick="toggleFavorite(this, '2510.01700v1', 'VaPR -- Vision-language Preference alignment for Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rohan Wadhawan, Fabrice Y Harel-Canada, Zi-Yi Dou, Suhaila Shakiah, Robinson Piramuthu, Nanyun Peng

**分类**: cs.AI, cs.CV, cs.LG

**发布日期**: 2025-10-02

**期刊**: COLM 2025

---

## 💡 一句话要点

**VaPR：通过视觉-语言偏好对齐提升大型视觉语言模型的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉语言模型` `偏好对齐` `硬负例挖掘` `推理能力` `大型语言模型`

## 📋 核心要点

1. 现有偏好微调方法忽略了合成偏好标注中存在的噪声，如风格和长度偏差，影响了LVLM的性能。
2. 论文提出基于LLM引导的响应编辑的硬负例生成框架，生成具有针对性错误但风格和长度相似的拒绝响应。
3. VaPR数据集和微调模型在多个基准测试中显著提升了LVLM的推理能力，并降低了回答“是”的倾向。

## 📝 摘要（中文）

本文提出了一种基于视觉-语言偏好对齐的推理方法，旨在解决大型视觉语言模型（LVLM）中存在的合成偏好标注噪声问题，特别是风格和长度偏差。为此，作者设计了一个基于LLM引导的响应编辑的硬负例响应生成框架，该框架能够生成具有目标性错误的拒绝响应，同时保持与接受响应在风格和长度上的相似性。利用该框架，构建了包含3万个高质量样本的VaPR数据集，并对LLaVA-V1.5、Qwen2VL和Qwen2.5VL（2B-13B大小）三个LVLM家族进行了微调。实验结果表明，VaPR模型在十个基准测试中取得了显著的性能提升，平均增益分别为6.5%（LLaVA）、4.0%（Qwen2VL）和1.5%（Qwen2.5VL），尤其在推理任务上表现突出。此外，VaPR还降低了LVLM（如LLaVA）在二元问题中回答“是”的倾向。该框架还可推广到开源LLM作为编辑器，使用GPT-4o合成的数据训练的模型性能接近使用GPT-4o训练的模型。数据、模型和代码已公开。

## 🔬 方法详解

**问题定义**：现有的大型视觉语言模型（LVLM）在进行偏好微调时，依赖于AI生成的反馈。然而，这些反馈中存在大量的噪声，特别是风格和长度上的偏差。这些偏差会影响模型学习到真正的人类偏好，从而限制了模型在推理任务上的表现。现有方法没有充分考虑到这些噪声，导致模型容易受到这些偏差的影响。

**核心思路**：论文的核心思路是通过生成高质量的硬负例来提高偏好微调的质量。具体来说，通过LLM引导的响应编辑，生成与接受响应在风格和长度上相似，但包含特定错误的拒绝响应。这样可以迫使模型更加关注语义上的差异，而不是仅仅依赖风格和长度等表面特征进行判断。

**技术框架**：VaPR框架主要包含两个阶段：1) 硬负例响应生成阶段：使用LLM（如GPT-4o）作为编辑器，对原始响应进行编辑，引入特定的错误，生成拒绝响应。2) 偏好微调阶段：使用生成的VaPR数据集，采用Direct Preference Optimization (DPO)等偏好优化算法，对LVLM进行微调。整个流程旨在对齐模型的偏好与人类的偏好，提升模型的推理能力。

**关键创新**：该论文的关键创新在于提出了一个硬负例响应生成框架，该框架能够生成具有针对性错误的拒绝响应，同时保持与接受响应在风格和长度上的相似性。这种方法有效地解决了现有偏好微调方法中存在的合成偏好标注噪声问题。此外，该框架具有通用性，可以推广到不同的LLM作为编辑器。

**关键设计**：在硬负例响应生成阶段，使用LLM作为编辑器，通过特定的prompt引导LLM引入不同类型的错误，例如事实错误、逻辑错误等。同时，通过控制LLM的生成过程，保证拒绝响应与接受响应在风格和长度上保持相似。在偏好微调阶段，采用DPO算法，并调整了DPO的超参数，以获得更好的性能。具体参数设置未知。

## 📊 实验亮点

VaPR模型在十个基准测试中取得了显著的性能提升，LLaVA、Qwen2VL和Qwen2.5VL的平均增益分别为6.5%、4.0%和1.5%。尤其在推理任务上表现突出。此外，VaPR还降低了LVLM（如LLaVA）在二元问题中回答“是”的倾向。使用开源LLM作为编辑器训练的模型性能接近使用GPT-4o训练的模型，表明该框架具有良好的泛化能力。

## 🎯 应用场景

VaPR的研究成果可应用于各种需要视觉和语言理解的场景，例如智能问答、视觉推理、机器人导航等。通过提高LVLM的推理能力，可以提升这些应用的用户体验和智能化水平。此外，该研究提出的硬负例生成框架也可以推广到其他模态，例如音频和文本，从而提升多模态模型的性能。

## 📄 摘要（原文）

> Preference finetuning methods like Direct Preference Optimization (DPO) with AI-generated feedback have shown promise in aligning Large Vision-Language Models (LVLMs) with human preferences. However, existing techniques overlook the prevalence of noise in synthetic preference annotations in the form of stylistic and length biases. To this end, we introduce a hard-negative response generation framework based on LLM-guided response editing, that produces rejected responses with targeted errors, maintaining stylistic and length similarity to the accepted ones. Using this framework, we develop the VaPR dataset, comprising 30K high-quality samples, to finetune three LVLM families: LLaVA-V1.5, Qwen2VL & Qwen2.5VL (2B-13B sizes). Our VaPR models deliver significant performance improvements across ten benchmarks, achieving average gains of 6.5% (LLaVA), 4.0% (Qwen2VL), and 1.5% (Qwen2.5VL), with notable improvements on reasoning tasks. A scaling analysis shows that performance consistently improves with data size, with LLaVA models benefiting even at smaller scales. Moreover, VaPR reduces the tendency to answer "Yes" in binary questions - addressing a common failure mode in LVLMs like LLaVA. Lastly, we show that the framework generalizes to open-source LLMs as editors, with models trained on VaPR-OS achieving ~99% of the performance of models trained on \name, which is synthesized using GPT-4o. Our data, models, and code can be found on the project page https://vap-r.github.io

