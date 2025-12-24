---
layout: default
title: "MSR-Align: Policy-Grounded Multimodal Alignment for Safety-Aware Reasoning in Vision-Language Models"
---

# MSR-Align: Policy-Grounded Multimodal Alignment for Safety-Aware Reasoning in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19257" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19257v2</a>
  <a href="https://arxiv.org/pdf/2506.19257.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19257v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19257v2', 'MSR-Align: Policy-Grounded Multimodal Alignment for Safety-Aware Reasoning in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinan Xia, Yilei Jiang, Yingshui Tan, Xiaoyong Zhu, Xiangyu Yue, Bo Zheng

**分类**: cs.CV, cs.CL

**发布日期**: 2025-06-24 (更新: 2025-10-21)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/Leigest)

---

## 💡 一句话要点

**提出MSR-Align以解决多模态模型安全对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `安全对齐` `视觉-语言模型` `政策推理` `数据集构建` `鲁棒性提升`

## 📋 核心要点

1. 现有的安全对齐方法无法有效应对多模态输入带来的复杂威胁，尤其是在视觉-语言模型中。
2. 本文提出MSR-Align数据集，支持基于政策的细粒度推理，旨在提高VLMs的安全性和鲁棒性。
3. 实验结果显示，微调VLMs后在MSR-Align上显著提升了对攻击的抵抗能力，同时保持了推理性能。

## 📝 摘要（中文）

视觉-语言模型（VLMs）在多模态推理任务中取得了显著进展，但也带来了新的安全风险，尤其是对有害多模态提示的脆弱性。现有的安全对齐方法主要针对单模态语言模型，无法有效应对多模态输入的复杂威胁。此外，当前的安全数据集缺乏细粒度的、基于政策的推理，无法有效对齐具备推理能力的VLMs。为此，本文提出了MSR-Align，一个高质量的多模态安全推理数据集，旨在填补这一空白。MSR-Align支持对视觉和文本模态的标准化安全政策进行细致的推理，实验表明，在MSR-Align上微调VLMs显著提高了对文本和视觉-语言攻击的鲁棒性，同时保持或提升了整体推理性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉-语言模型在面对多模态输入时的安全对齐问题。现有方法主要针对单模态模型，无法有效应对多模态输入的复杂性和潜在威胁。

**核心思路**：提出MSR-Align数据集，强调多模态的多样性和基于政策的推理，以增强VLMs的安全性和鲁棒性。通过细致的推理和质量过滤，确保数据集的高质量和有效性。

**技术框架**：MSR-Align的数据生成流程包括多模态数据的收集、政策的标准化定义、以及使用强大的多模态评审者进行质量过滤。整体架构分为数据生成、模型微调和性能评估三个主要阶段。

**关键创新**：MSR-Align的核心创新在于其高质量的多模态安全推理数据集，填补了现有数据集在细粒度和政策对齐方面的空白。这一设计使得VLMs能够更好地理解和应对多模态输入的安全挑战。

**关键设计**：在数据生成过程中，采用了多样化的模态组合和严格的质量控制，确保每个样本都能有效支持基于政策的推理。同时，微调过程中使用了特定的损失函数，以优化模型在安全性和推理能力上的表现。

## 📊 实验亮点

实验结果表明，在MSR-Align上微调的VLMs在面对文本和视觉-语言攻击时，鲁棒性显著提高，具体提升幅度达到XX%（具体数据待补充），同时保持或提升了整体推理性能，验证了数据集的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、智能监控和人机交互等场景，能够有效提升视觉-语言模型在复杂环境中的安全性和可靠性。随着多模态技术的发展，MSR-Align为未来的安全对齐研究提供了重要基础，具有广泛的实际价值和影响力。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have achieved remarkable progress in multimodal reasoning tasks through enhanced chain-of-thought capabilities. However, this advancement also introduces novel safety risks, as these models become increasingly vulnerable to harmful multimodal prompts that can trigger unethical or unsafe behaviors. Existing safety alignment approaches, primarily designed for unimodal language models, fall short in addressing the complex and nuanced threats posed by multimodal inputs. Moreover, current safety datasets lack the fine-grained, policy-grounded reasoning required to robustly align reasoning-capable VLMs. In this work, we introduce {MSR-Align}, a high-quality Multimodal Safety Reasoning dataset tailored to bridge this gap. MSR-Align supports fine-grained, deliberative reasoning over standardized safety policies across both vision and text modalities. Our data generation pipeline emphasizes multimodal diversity, policy-grounded reasoning, and rigorous quality filtering using strong multimodal judges. Extensive experiments demonstrate that fine-tuning VLMs on MSR-Align substantially improves robustness against both textual and vision-language jailbreak attacks, while preserving or enhancing general reasoning performance. MSR-Align provides a scalable and effective foundation for advancing the safety alignment of reasoning-capable VLMs. Our dataset is made publicly available at https://huggingface.co/datasets/Leigest/MSR-Align.

