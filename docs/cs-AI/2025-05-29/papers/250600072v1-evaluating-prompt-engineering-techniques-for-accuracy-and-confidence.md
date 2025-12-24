---
layout: default
title: Evaluating Prompt Engineering Techniques for Accuracy and Confidence Elicitation in Medical LLMs
---

# Evaluating Prompt Engineering Techniques for Accuracy and Confidence Elicitation in Medical LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00072" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00072v1</a>
  <a href="https://arxiv.org/pdf/2506.00072.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00072v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00072v1', 'Evaluating Prompt Engineering Techniques for Accuracy and Confidence Elicitation in Medical LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nariman Naderi, Zahra Atf, Peter R Lewis, Aref Mahjoub far, Seyed Amir Ahmad Safavi-Naini, Ali Soroush

**分类**: cs.CY, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-29

**备注**: This paper was accepted for presentation at the 7th International Workshop on EXplainable, Trustworthy, and Responsible AI and Multi-Agent Systems (EXTRAAMAS 2025). Workshop website: https://extraamas.ehealth.hevs.ch/index.html

---

## 💡 一句话要点

**评估提示工程技术以提升医疗领域大语言模型的准确性与信心**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `提示工程` `医疗AI` `信心校准` `模型评估` `准确性提升` `过度自信` `风险管理`

## 📋 核心要点

1. 现有方法在医疗领域的应用中，准确性与信心引导之间存在矛盾，导致决策风险增加。
2. 本文提出通过多种提示工程技术，系统评估其对大语言模型在医疗任务中准确性和信心的影响。
3. 实验结果显示，Chain-of-Thought提示提高了准确性，但也引发过度自信，强调了对信心的校准需求。

## 📝 摘要（中文）

本文研究了提示工程技术如何影响应用于医疗领域的大语言模型（LLMs）的准确性和信心引导。通过对多个专业的波斯语考试问题进行分层数据集评估，测试了五种LLM（GPT-4o、o3-mini、Llama-3.3-70b、Llama-3.1-8b和DeepSeek-v3）在156种配置下的表现。这些配置在温度设置、提示风格和信心量表上有所不同。结果表明，Chain-of-Thought提示提高了准确性，但也导致了过度自信，强调了校准的必要性。情感提示进一步增加了信心，可能导致不良决策。较小的模型在所有指标上表现不佳，而专有模型虽然准确性较高，但仍缺乏校准信心。这些结果表明，提示工程必须同时关注准确性和不确定性，以在高风险医疗任务中有效。

## 🔬 方法详解

**问题定义**：本文旨在解决医疗领域大语言模型在准确性与信心引导方面的不足，现有方法未能有效平衡这两者，导致潜在的决策风险。

**核心思路**：通过多种提示工程技术的组合，评估其对模型性能的影响，特别是在高风险医疗环境中，确保模型的输出既准确又具有可靠的信心水平。

**技术框架**：研究采用了分层数据集，包含多个专业的波斯语考试问题，评估了五种不同的LLM在156种配置下的表现，涉及温度设置、提示风格和信心量表等多个维度。

**关键创新**：最重要的创新在于系统性地评估不同提示风格对模型准确性和信心的影响，特别是Chain-of-Thought和情感提示的使用，揭示了过度自信的风险。

**关键设计**：实验中使用了多种温度设置（0.3、0.7、1.0）、不同的提示风格（Chain-of-Thought、Few-Shot、情感、专家模仿）以及信心量表（1-10、1-100），并通过AUC-ROC、Brier Score和期望校准误差（ECE）等指标进行评估。

## 📊 实验亮点

实验结果显示，Chain-of-Thought提示在提高模型准确性方面表现突出，但同时也导致了过度自信的现象。较小的模型（如Llama-3.1-8b）在所有评估指标上均表现不佳，而专有模型虽然准确性较高，但信心校准仍显不足。这些发现强调了在高风险医疗任务中，提示工程需同时关注准确性与不确定性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗诊断支持系统、患者咨询和医疗教育等。通过优化大语言模型的提示工程，可以提升医疗决策的准确性与信心，从而降低医疗错误的风险，增强患者安全。未来，该研究可能推动更广泛的AI在医疗领域的应用，提升整体医疗服务质量。

## 📄 摘要（原文）

> This paper investigates how prompt engineering techniques impact both accuracy and confidence elicitation in Large Language Models (LLMs) applied to medical contexts. Using a stratified dataset of Persian board exam questions across multiple specialties, we evaluated five LLMs - GPT-4o, o3-mini, Llama-3.3-70b, Llama-3.1-8b, and DeepSeek-v3 - across 156 configurations. These configurations varied in temperature settings (0.3, 0.7, 1.0), prompt styles (Chain-of-Thought, Few-Shot, Emotional, Expert Mimicry), and confidence scales (1-10, 1-100). We used AUC-ROC, Brier Score, and Expected Calibration Error (ECE) to evaluate alignment between confidence and actual performance. Chain-of-Thought prompts improved accuracy but also led to overconfidence, highlighting the need for calibration. Emotional prompting further inflated confidence, risking poor decisions. Smaller models like Llama-3.1-8b underperformed across all metrics, while proprietary models showed higher accuracy but still lacked calibrated confidence. These results suggest prompt engineering must address both accuracy and uncertainty to be effective in high-stakes medical tasks.

