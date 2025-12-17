---
layout: default
title: Adapting General-Purpose Foundation Models for X-ray Ptychography in Low-Data Regimes
---

# Adapting General-Purpose Foundation Models for X-ray Ptychography in Low-Data Regimes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02503" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02503</a>
  <a href="https://arxiv.org/pdf/2511.02503.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02503" onclick="toggleFavorite(this, '2511.02503', 'Adapting General-Purpose Foundation Models for X-ray Ptychography in Low-Data Regimes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Robinson Umeike, Neil Getty, Yin Xiangyu, Yi Jiang

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**针对低数据量X射线衍射成像，提出通用基础模型自适应方法PtychoBench**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `X射线衍射成像` `基础模型` `领域适配` `监督微调` `上下文学习` `多模态学习` `低数据学习` `PtychoBench`

## 📋 核心要点

1. 现有先进显微镜工作流程自动化程度低，缺乏针对性强、数据高效的AI解决方案。
2. 提出PtychoBench基准，系统评估监督微调（SFT）和上下文学习（ICL）两种领域适配策略。
3. 实验表明，最佳策略取决于任务模态，视觉任务SFT+ICL互补，文本任务ICL更优。

## 📝 摘要（中文）

先进显微镜工作流程的自动化是关键目标，而语言模型（LLM）和视觉-语言模型（VLM）等基础模型显示出巨大潜力。然而，将这些通用模型适配到专门的科学任务至关重要，且最佳的领域适配策略通常不明确。为此，我们引入了PtychoBench，这是一个用于衍射成像分析的新型多模态、多任务基准。利用此基准，我们系统地比较了两种专门化策略：监督微调（SFT）和上下文学习（ICL）。我们在数据稀缺的情况下，使用VLM评估了视觉伪影检测任务，并使用LLM评估了文本参数推荐任务。我们的研究结果表明，最佳的专门化路径取决于任务模态。对于视觉任务，SFT和ICL高度互补，通过上下文感知示例引导的微调模型实现了最高的平均性能（Micro-F1为0.728）。相反，对于文本任务，大型基础模型上的ICL是更优越的策略，达到了峰值Micro-F1为0.847，优于强大的“超级专家”SFT模型（0-shot Micro-F1为0.839）。我们还证实了上下文感知提示的优越性，并识别了微调模型中一致的上下文干扰现象。这些结果以GPT-4o和基于DINOv3的分类器等强大基线为基准，为科学中的人工智能提供了关键观察：在我们的基准中，最佳的专门化路径取决于任务模态，为开发更有效的基于科学的智能体系统提供了一个清晰的框架。

## 🔬 方法详解

**问题定义**：论文旨在解决在低数据量情况下，如何有效地将通用基础模型（如LLM和VLM）应用于X射线衍射成像（Ptychography）中的特定任务，例如视觉伪影检测和文本参数推荐。现有方法要么需要大量标注数据进行微调，要么泛化能力不足，难以适应科学领域的专业任务。

**核心思路**：论文的核心思路是通过构建一个多模态、多任务的基准测试平台PtychoBench，系统性地比较和分析两种主要的领域适配策略：监督微调（SFT）和上下文学习（ICL）。通过对比不同策略在不同任务上的表现，揭示最佳的适配路径，并为未来开发更有效的科学智能体系统提供指导。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 构建PtychoBench基准数据集，包含多模态数据（图像和文本）和多个任务（视觉伪影检测和文本参数推荐）；2) 实施并比较两种领域适配策略：SFT和ICL；3) 使用强大的基线模型（如GPT-4o和DINOv3）进行性能对比；4) 分析实验结果，识别最佳适配策略，并解释其背后的原因。

**关键创新**：论文的关键创新在于：1) 提出了PtychoBench基准，为X射线衍射成像领域的AI研究提供了一个标准化的评估平台；2) 系统性地比较了SFT和ICL两种领域适配策略，揭示了它们在不同任务上的优劣；3) 发现了上下文感知提示的优越性，并识别了微调模型中存在的上下文干扰现象。

**关键设计**：在视觉伪影检测任务中，论文使用了基于DINOv3的分类器作为基线，并探索了SFT和ICL的组合策略。在文本参数推荐任务中，论文使用了LLM，并比较了不同规模的模型和不同的提示策略。论文还特别关注了低数据量的情况，并设计了相应的实验来评估不同策略的鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.02503/key_metrics.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.02503/artifact_type_counts.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.02503/sample_type_counts.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，对于视觉伪影检测任务，SFT和ICL互补，微调模型在上下文感知示例引导下Micro-F1达到0.728。对于文本参数推荐任务，ICL优于SFT，Micro-F1达到0.847，超过了“超级专家”SFT模型（0.839）。同时，验证了上下文感知提示的有效性，并发现了微调模型中的上下文干扰现象。

## 🎯 应用场景

该研究成果可应用于自动化显微镜工作流程，加速科学发现。通过优化模型适配策略，能更有效地利用AI进行图像分析、参数优化等任务，降低对人工干预的依赖，提升科研效率。未来可扩展到其他科学领域，促进AI在科学研究中的更广泛应用。

## 📄 摘要（原文）

> The automation of workflows in advanced microscopy is a key goal where foundation models like Language Models (LLMs) and Vision-Language Models (VLMs) show great potential. However, adapting these general-purpose models for specialized scientific tasks is critical, and the optimal domain adaptation strategy is often unclear. To address this, we introduce PtychoBench, a new multi-modal, multi-task benchmark for ptychographic analysis. Using this benchmark, we systematically compare two specialization strategies: Supervised Fine-Tuning (SFT) and In-Context Learning (ICL). We evaluate these strategies on a visual artifact detection task with VLMs and a textual parameter recommendation task with LLMs in a data-scarce regime. Our findings reveal that the optimal specialization pathway is task-dependent. For the visual task, SFT and ICL are highly complementary, with a fine-tuned model guided by context-aware examples achieving the highest mean performance (Micro-F1 of 0.728). Conversely, for the textual task, ICL on a large base model is the superior strategy, reaching a peak Micro-F1 of 0.847 and outperforming a powerful "super-expert" SFT model (0-shot Micro-F1 of 0.839). We also confirm the superiority of context-aware prompting and identify a consistent contextual interference phenomenon in fine-tuned models. These results, benchmarked against strong baselines including GPT-4o and a DINOv3-based classifier, offer key observations for AI in science: the optimal specialization path in our benchmark is dependent on the task modality, offering a clear framework for developing more effective science-based agentic systems.

