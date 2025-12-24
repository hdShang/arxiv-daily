---
layout: default
title: "Beyond the Score: Uncertainty-Calibrated LLMs for Automated Essay Assessment"
---

# Beyond the Score: Uncertainty-Calibrated LLMs for Automated Essay Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15926" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15926v1</a>
  <a href="https://arxiv.org/pdf/2509.15926.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15926v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15926v1', 'Beyond the Score: Uncertainty-Calibrated LLMs for Automated Essay Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmed Karim, Qiao Wang, Zheng Yuan

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-19

**备注**: Accepted at EMNLP 2025 (Main Conference). Camera-ready version

---

## 💡 一句话要点

**提出基于不确定性校准的大语言模型，用于提升自动作文评分系统的可靠性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动作文评分` `不确定性校准` `Conformal Prediction` `大语言模型` `教育应用`

## 📋 核心要点

1. 现有自动作文评分系统缺乏置信度评估，限制了其在高风险场景中的应用。
2. 利用conformal prediction为大语言模型提供集合值输出，并保证覆盖率，从而校准模型的不确定性。
3. 实验表明，校准后的开源中型LLM在满足覆盖目标的同时，保持了预测集的紧凑性。

## 📝 摘要（中文）

自动作文评分(AES)系统在某些公共基准测试中已接近人类水平，但实际应用，尤其是在高风险考试中，仍然有限。一个主要障碍是大多数模型输出单一分数，缺乏置信度衡量或解释。本文利用conformal prediction解决这个问题，这是一种与分布无关的封装方法，使任何分类器都能输出集合值，并具有正式的覆盖保证。在三个不同的语料库(ASAP、TOEFL11、Cambridge-FCE)上微调两个开源大语言模型(Llama-3 8B和Qwen-2.5 3B)，并在90%的风险水平下进行校准。使用UAcc评估可靠性，这是一种不确定性感知准确率，奖励模型既正确又简洁。据我们所知，这是第一项将conformal prediction和UAcc结合用于作文评分的工作。校准后的模型始终满足覆盖目标，同时保持预测集紧凑，表明开源中型LLM已经可以支持教师参与的AES；我们讨论了未来的扩展和更广泛的用户研究。

## 🔬 方法详解

**问题定义**：自动作文评分(AES)系统虽然在准确率上有所提升，但缺乏对评分结果的置信度评估，导致难以在高风险场景中应用。现有方法通常只输出一个单一的分数，没有提供任何关于模型预测不确定性的信息，这使得用户难以信任和理解模型的评分结果。

**核心思路**：本文的核心思路是利用conformal prediction来校准大语言模型的不确定性。Conformal prediction是一种与分布无关的方法，可以为任何分类器提供集合值的输出，并保证一定的覆盖率。通过将conformal prediction应用于AES系统，可以使模型不仅输出一个分数，还输出一个置信区间，从而让用户更好地理解和信任模型的评分结果。

**技术框架**：本文的技术框架主要包括以下几个步骤：1)选择预训练的大语言模型（Llama-3 8B和Qwen-2.5 3B）；2)在三个不同的作文语料库（ASAP、TOEFL11、Cambridge-FCE）上对模型进行微调；3)使用conformal prediction对微调后的模型进行校准，使其能够输出集合值的预测结果；4)使用UAcc指标评估校准后模型的可靠性。

**关键创新**：本文最重要的技术创新点是将conformal prediction应用于自动作文评分任务。与现有方法相比，本文的方法不仅可以提高评分的准确率，还可以提供对评分结果的置信度评估。这是第一项将conformal prediction和UAcc结合用于作文评分的工作。

**关键设计**：本文的关键设计包括：1)选择合适的预训练大语言模型；2)选择合适的作文语料库进行微调；3)选择合适的风险水平（90%）进行校准；4)使用UAcc指标评估模型的可靠性。UAcc是一种不确定性感知准确率，它奖励模型既正确又简洁。具体而言，UAcc的计算方式是：对于每个样本，如果模型的预测结果包含真实标签，则UAcc增加一个值，该值与预测集合的大小成反比。这样，模型既要保证预测结果的覆盖率，又要尽量减小预测集合的大小。

## 📊 实验亮点

实验结果表明，经过conformal prediction校准后的Llama-3 8B和Qwen-2.5 3B模型，在三个不同的作文语料库上均能达到90%的覆盖率目标，同时保持预测集合的紧凑性。这表明，开源中型LLM已经可以支持教师参与的AES，并为未来的扩展和更广泛的用户研究奠定了基础。

## 🎯 应用场景

该研究成果可应用于各种教育场景，例如在线教育平台、作文批改软件等。通过提供带有置信度评估的自动作文评分，可以帮助教师更有效地进行教学，并提高学生的学习效率。此外，该技术还可以应用于其他需要高可靠性的自然语言处理任务，例如机器翻译、文本摘要等。

## 📄 摘要（原文）

> Automated Essay Scoring (AES) systems now reach near human agreement on some public benchmarks, yet real-world adoption, especially in high-stakes examinations, remains limited. A principal obstacle is that most models output a single score without any accompanying measure of confidence or explanation. We address this gap with conformal prediction, a distribution-free wrapper that equips any classifier with set-valued outputs and formal coverage guarantees. Two open-source large language models (Llama-3 8B and Qwen-2.5 3B) are fine-tuned on three diverse corpora (ASAP, TOEFL11, Cambridge-FCE) and calibrated at a 90 percent risk level. Reliability is assessed with UAcc, an uncertainty-aware accuracy that rewards models for being both correct and concise. To our knowledge, this is the first work to combine conformal prediction and UAcc for essay scoring. The calibrated models consistently meet the coverage target while keeping prediction sets compact, indicating that open-source, mid-sized LLMs can already support teacher-in-the-loop AES; we discuss scaling and broader user studies as future work.

