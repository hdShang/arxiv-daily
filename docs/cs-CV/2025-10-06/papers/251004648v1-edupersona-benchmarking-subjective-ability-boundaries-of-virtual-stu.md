---
layout: default
title: EduPersona: Benchmarking Subjective Ability Boundaries of Virtual Student Agents
---

# EduPersona: Benchmarking Subjective Ability Boundaries of Virtual Student Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04648" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04648v1</a>
  <a href="https://arxiv.org/pdf/2510.04648.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04648v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.04648v1', 'EduPersona: Benchmarking Subjective Ability Boundaries of Virtual Student Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Buyuan Zhu, Shiyu Hu, Yiping Ma, Yuanming Zhang, Kang Hao Cheong

**分类**: cs.CV, cs.CY

**发布日期**: 2025-10-06

**备注**: Preprint, Under review

---

## 💡 一句话要点

**EduPersona：评估虚拟学生Agent主观能力的基准测试**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚拟学生Agent` `主观能力评估` `基准测试` `人格建模` `教育人工智能`

## 📋 核心要点

1. 现有虚拟学生Agent的主观能力评估不足，限制了其在教育领域的可靠应用。
2. EduPersona通过构建大规模基准数据集，并解耦主观能力评估为三个渐进式任务。
3. 实验表明，在EduPersona上微调的模型在连贯性、真实感和一致性方面均有显著提升。

## 📝 摘要（中文）

随着大型语言模型日益融入教育领域，虚拟学生Agent在课堂模拟和教师培训中变得至关重要。然而，它们面向课堂的主观能力在很大程度上尚未得到评估，这限制了对模型边界的理解，并阻碍了可信部署。我们提出了EduPersona，这是一个大规模基准测试，涵盖两种语言、三个科目和基于大五人格理论的十种人格类型。该数据集包含1308轮真实的课堂对话，对应12814轮师生问答，并通过人格风格化扩展到大约10倍的规模（12.8万轮），为评估提供了坚实的基础。在此基础上，我们将难以量化的主观表现分解为三个渐进式任务：任务1基本连贯性（行为、情感、表达和声音是否与课堂环境一致），任务2学生真实感，以及任务3长期人格一致性，从而建立了一个基于教育理论和研究价值的评估框架。我们对三个具有代表性的LLM进行了系统实验，比较了它们的原始版本和在EduPersona上训练的十个经过人格微调的变体。结果显示，所有任务的平均改进都是一致且显著的：任务1 +33.6%，任务2 +30.6%，任务3 +14.9%。这些改进突出了数据集的有效性和研究价值，同时也揭示了人格建模的异构难度。总之，EduPersona提供了第一个以主观能力为中心的课堂基准，建立了一个解耦且可验证的研究范式，我们将开源数据集和框架，以支持更广泛的研究社区推进可信和类人的人工智能在教育中的应用。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在教育领域，特别是作为虚拟学生Agent应用时，其主观能力（如人格一致性、情感表达的真实性等）缺乏有效的评估手段。这导致难以了解这些模型的边界，并阻碍了它们在教育场景中的可信部署。现有方法难以量化这些主观能力，缺乏针对教育场景的细粒度评估。

**核心思路**：EduPersona的核心思路是通过构建一个大规模、多维度的数据集，并设计一套解耦的评估任务，从而对虚拟学生Agent的主观能力进行量化评估。该方法将主观能力分解为多个可验证的子任务，使得评估过程更加透明和可控。通过人格风格化扩展数据集，增强模型的泛化能力。

**技术框架**：EduPersona的整体框架包括以下几个主要部分：
1. **数据集构建**：收集真实的课堂对话数据，并基于大五人格理论定义十种不同的人格类型。通过人工标注和风格化生成大规模数据集。
2. **任务分解**：将主观能力评估分解为三个渐进式任务：基本连贯性（TASK1）、学生真实感（TASK2）和长期人格一致性（TASK3）。
3. **模型训练与评估**：使用EduPersona数据集对LLM进行人格微调，并在三个任务上进行评估，比较微调前后模型的性能。

**关键创新**：EduPersona的关键创新在于：
1. **首个面向课堂主观能力的基准测试**：专注于评估虚拟学生Agent在教育场景下的主观能力，填补了现有研究的空白。
2. **解耦的评估范式**：将主观能力分解为多个可验证的子任务，使得评估过程更加透明和可控。
3. **大规模人格风格化数据集**：通过人格风格化扩展数据集，增强模型的泛化能力。

**关键设计**：EduPersona的关键设计包括：
1. **人格类型定义**：基于大五人格理论，定义了十种不同的人格类型，覆盖了学生群体的多样性。
2. **任务设计**：TASK1评估基本连贯性，关注行为、情感、表达和声音是否与课堂环境一致；TASK2评估学生真实感，关注Agent的行为是否符合学生的身份；TASK3评估长期人格一致性，关注Agent在长期对话中是否保持一致的人格特征。
3. **评估指标**：针对每个任务，设计了相应的评估指标，例如，使用困惑度（perplexity）评估连贯性，使用人工评估判断真实感和一致性。

## 📊 实验亮点

实验结果表明，在EduPersona数据集上进行人格微调后，LLM在三个评估任务上均取得了显著提升：TASK1（基本连贯性）提升33.6%，TASK2（学生真实感）提升30.6%，TASK3（长期人格一致性）提升14.9%。这些结果验证了EduPersona数据集的有效性，并表明人格微调可以显著提高虚拟学生Agent的主观能力。

## 🎯 应用场景

EduPersona的研究成果可应用于开发更逼真、更可信的虚拟学生Agent，用于课堂模拟、教师培训和个性化学习。通过评估和提升Agent的主观能力，可以提高教学效果，并为学生提供更具个性化的学习体验。该研究还有助于推动人工智能在教育领域的更广泛应用。

## 📄 摘要（原文）

> As large language models are increasingly integrated into education, virtual student agents are becoming vital for classroom simulation and teacher training. Yet their classroom-oriented subjective abilities remain largely unassessed, limiting understanding of model boundaries and hindering trustworthy deployment. We present EduPersona, a large-scale benchmark spanning two languages, three subjects, and ten persona types based on the Big Five theory. The dataset contains 1,308 authentic classroom dialogue rounds, corresponding to 12,814 teacher-student Q&A turns, and is further expanded through persona stylization into roughly 10 times larger scale (128k turns), providing a solid foundation for evaluation. Building on this resource, we decompose hard-to-quantify subjective performance into three progressive tasks: TASK1 basic coherence (whether behavior, emotion, expression, and voice align with classroom context), TASK2 student realism, and TASK3 long-term persona consistency, thereby establishing an evaluation framework grounded in educational theory and research value. We conduct systematic experiments on three representative LLMs, comparing their original versions with ten persona-fine-tuned variants trained on EduPersona. Results show consistent and significant average improvements across all tasks: TASK1 +33.6%, TASK2 +30.6%, and TASK3 +14.9%. These improvements highlight the dataset's effectiveness and research value, while also revealing the heterogeneous difficulty of persona modeling. In summary, EduPersona delivers the first classroom benchmark centered on subjective abilities, establishes a decoupled and verifiable research paradigm, and we will open-source both the dataset and the framework to support the broader research community in advancing trustworthy and human-like AI for education.

