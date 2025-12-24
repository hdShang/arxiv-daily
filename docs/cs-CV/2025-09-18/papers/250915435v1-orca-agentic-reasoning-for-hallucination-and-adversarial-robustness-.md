---
layout: default
title: "ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models"
---

# ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15435" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15435v1</a>
  <a href="https://arxiv.org/pdf/2509.15435.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15435v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15435v1', 'ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chung-En Johnny Yu, Hsuan-Chih, Chen, Brian Jalaian, Nathaniel D. Bastian

**分类**: cs.CV, cs.AI, cs.MA

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**提出ORCA框架，通过智能体推理提升视觉-语言模型在幻觉抑制和对抗鲁棒性上的表现。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `幻觉抑制` `对抗鲁棒性` `智能体推理` `多模态学习`

## 📋 核心要点

1. 现有大型视觉-语言模型易受幻觉和对抗攻击影响，限制了其在实际应用中的可靠性。
2. ORCA框架通过智能体推理，利用小型视觉模型在测试时进行结构化推理，提升模型的准确性和鲁棒性。
3. 实验表明，ORCA在幻觉抑制和对抗攻击防御方面均有显著提升，无需模型内部访问或重新训练。

## 📝 摘要（中文）

大型视觉-语言模型(LVLMs)展现了强大的多模态能力，但仍然容易受到内在错误导致的幻觉和外部攻击导致的对抗样本的影响，这限制了它们在实际应用中的可靠性。我们提出了ORCA，一个智能体推理框架，通过测试时结构化推理和一套小型视觉模型（小于30亿参数）来提高预训练LVLMs的事实准确性和对抗鲁棒性。ORCA通过观察-推理-评论-行动循环运行，使用证据性问题查询多个视觉工具，验证跨模型的不一致性，并迭代地改进预测，而无需访问模型内部或重新训练。ORCA还存储中间推理轨迹，这支持可审计的决策。虽然主要设计用于减轻对象级别的幻觉，但ORCA也表现出涌现的对抗鲁棒性，而无需对抗训练或防御机制。我们在三种设置下评估ORCA：（1）幻觉基准测试中的干净图像，（2）没有防御的对抗扰动图像，以及（3）应用防御的对抗扰动图像。在POPE幻觉基准测试中，ORCA将独立LVLM的性能提高了+3.64％至+40.67％。在POPE上的对抗扰动下，ORCA在LVLM上的平均准确度提高了+20.11％。当与AMBER图像上对抗扰动的防御技术相结合时，ORCA进一步提高了独立LVLM的性能，在评估指标上的增益范围为+1.20％至+48.00％。这些结果表明，ORCA为构建更可靠和鲁棒的多模态系统提供了一条有希望的途径。

## 🔬 方法详解

**问题定义**：大型视觉-语言模型（LVLMs）虽然功能强大，但容易产生幻觉（hallucination），即生成与图像内容不符的信息。此外，LVLMs也容易受到对抗攻击的影响，即使是微小的图像扰动也可能导致模型产生错误的输出。现有方法通常需要大量的对抗训练或复杂的防御机制，且效果有限。

**核心思路**：ORCA的核心思路是将LVLM视为一个智能体，通过模拟人类的推理过程来提高其可靠性。ORCA利用多个小型视觉模型作为外部工具，通过观察、推理、评论和行动的循环迭代，验证和修正LVLM的输出，从而减少幻觉并提高对抗鲁棒性。这种方法无需修改LVLM的内部结构或进行额外的训练。

**技术框架**：ORCA框架包含以下几个主要模块：
1. **Observe（观察）**：LVLM接收图像输入并生成初始预测。
2. **Reason（推理）**：ORCA根据初始预测，生成一系列证据性问题，并使用小型视觉模型（例如目标检测器、图像分割模型）作为外部工具来回答这些问题。
3. **Critique（评论）**：ORCA比较LVLM的初始预测和外部工具的回答，检测不一致性。
4. **Act（行动）**：根据不一致性检测结果，ORCA修正LVLM的预测，并重复上述循环，直到预测结果稳定或达到最大迭代次数。ORCA还会记录中间推理过程，以便进行审计和调试。

**关键创新**：ORCA的关键创新在于其智能体推理框架，它将LVLM与多个小型视觉模型结合，通过迭代的验证和修正过程来提高模型的可靠性。与传统的对抗训练或防御机制不同，ORCA无需修改LVLM的内部结构或进行额外的训练，而是通过外部推理来增强模型的性能。此外，ORCA的推理过程是可解释的，可以帮助理解模型做出决策的原因。

**关键设计**：ORCA的关键设计包括：
1. **证据性问题生成**：根据LVLM的初始预测，设计合适的证据性问题，以便外部视觉模型能够提供有用的信息。
2. **不一致性检测**：设计有效的算法来比较LVLM的预测和外部视觉模型的回答，检测不一致性。
3. **预测修正**：根据不一致性检测结果，设计合适的策略来修正LVLM的预测。
4. **迭代次数**：设置合适的迭代次数，以在性能和计算成本之间取得平衡。

## 📊 实验亮点

实验结果表明，ORCA在POPE幻觉基准测试中，将独立LVLM的性能提高了+3.64％至+40.67％。在对抗扰动下，ORCA在LVLM上的平均准确度提高了+20.11％。当与AMBER图像上对抗扰动的防御技术相结合时，ORCA进一步提高了独立LVLM的性能，在评估指标上的增益范围为+1.20％至+48.00％。这些结果证明了ORCA在提高视觉-语言模型可靠性和鲁棒性方面的有效性。

## 🎯 应用场景

ORCA框架具有广泛的应用前景，例如在自动驾驶、医疗诊断、智能客服等领域，可以提高视觉-语言模型的可靠性和安全性。通过减少幻觉和提高对抗鲁棒性，ORCA可以帮助构建更加值得信赖的多模态人工智能系统，从而更好地服务于人类社会。未来，ORCA可以进一步扩展到更多的应用场景和任务中。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) exhibit strong multimodal capabilities but remain vulnerable to hallucinations from intrinsic errors and adversarial attacks from external exploitations, limiting their reliability in real-world applications. We present ORCA, an agentic reasoning framework that improves the factual accuracy and adversarial robustness of pretrained LVLMs through test-time structured inference reasoning with a suite of small vision models (less than 3B parameters). ORCA operates via an Observe--Reason--Critique--Act loop, querying multiple visual tools with evidential questions, validating cross-model inconsistencies, and refining predictions iteratively without access to model internals or retraining. ORCA also stores intermediate reasoning traces, which supports auditable decision-making. Though designed primarily to mitigate object-level hallucinations, ORCA also exhibits emergent adversarial robustness without requiring adversarial training or defense mechanisms. We evaluate ORCA across three settings: (1) clean images on hallucination benchmarks, (2) adversarially perturbed images without defense, and (3) adversarially perturbed images with defense applied. On the POPE hallucination benchmark, ORCA improves standalone LVLM performance by +3.64\% to +40.67\% across different subsets. Under adversarial perturbations on POPE, ORCA achieves an average accuracy gain of +20.11\% across LVLMs. When combined with defense techniques on adversarially perturbed AMBER images, ORCA further improves standalone LVLM performance, with gains ranging from +1.20\% to +48.00\% across evaluation metrics. These results demonstrate that ORCA offers a promising path toward building more reliable and robust multimodal systems.

