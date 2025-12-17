---
layout: default
title: Boosting Multi-modal Keyphrase Prediction with Dynamic Chain-of-Thought in Vision-Language Models
---

# Boosting Multi-modal Keyphrase Prediction with Dynamic Chain-of-Thought in Vision-Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.09358" target="_blank" class="toolbar-btn">arXiv: 2510.09358v1</a>
    <a href="https://arxiv.org/pdf/2510.09358.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09358v1" 
            onclick="toggleFavorite(this, '2510.09358v1', 'Boosting Multi-modal Keyphrase Prediction with Dynamic Chain-of-Thought in Vision-Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Qihang Ma, Shengyu Li, Jie Tang, Dingkang Yang, Shaodong Chen, Yingyi Zhang, Chao Feng, Jiao Ran

**分类**: cs.CV

**发布日期**: 2025-10-10

**备注**: EMNLP2025. Code is avaible at https://github.com/bytedance/DynamicCoT

**🔗 代码/项目**: [GITHUB](https://github.com/bytedance/DynamicCoT)

---

## 💡 一句话要点

**提出动态链式思考方法，提升视觉-语言模型在多模态关键短语预测任务上的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态关键短语预测` `视觉-语言模型` `链式思考` `动态链式思考` `模型微调` `零样本学习` `监督学习`

## 📋 核心要点

1. 现有MMKP方法在处理数据缺失和未见场景时存在不足，且现有benchmark存在训练集和测试集重叠问题，导致模型能力被高估。
2. 论文提出利用视觉-语言模型(VLM)解决MMKP任务，并引入动态链式思考(Dynamic CoT)策略，提升VLM的复杂推理能力。
3. 实验结果表明，所提出的Dynamic CoT策略在多个数据集上有效提升了MMKP的性能，验证了该方法的有效性。

## 📝 摘要（中文）

多模态关键短语预测(MMKP)旨在通过整合多种模态的输入信息，生成一组结论性的短语，从而超越仅依赖文本的方法。传统的多模态方法在处理具有挑战性的缺失和未见场景时存在显著局限性。此外，我们发现现有基准测试由于训练测试中存在显著重叠，高估了模型的能力。在这项工作中，我们提出利用视觉-语言模型(VLM)来解决MMKP任务。首先，我们使用两种广泛使用的策略，例如零样本和监督微调(SFT)来评估VLM的下限性能。接下来，为了提高VLM的复杂推理能力，我们采用Fine-tune-CoT，它利用教师模型生成的高质量CoT推理数据来微调较小的模型。最后，为了解决“过度思考”现象，我们提出了一种动态CoT策略，该策略在训练期间自适应地注入CoT数据，使模型能够在推理阶段灵活地利用其推理能力。我们在各种数据集上评估了所提出的策略，实验结果证明了所提出方法的有效性。代码可在https://github.com/bytedance/DynamicCoT获得。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态关键短语预测（MMKP）任务中，现有方法在处理数据缺失、未见场景以及训练测试数据重叠等问题上的不足。现有方法难以充分利用多模态信息进行有效推理，导致预测性能受限。

**核心思路**：论文的核心思路是利用视觉-语言模型（VLM）强大的多模态理解能力，并结合链式思考（CoT）方法来增强模型的推理能力。为了避免CoT带来的“过度思考”问题，提出了动态CoT策略，使模型能够自适应地利用推理能力。

**技术框架**：整体框架包括以下几个阶段：1) 使用零样本和监督微调（SFT）方法评估VLM在MMKP任务上的下限性能。2) 采用Fine-tune-CoT方法，利用教师模型生成的高质量CoT数据微调VLM，提升其推理能力。3) 引入动态CoT策略，在训练过程中自适应地注入CoT数据，使模型在推理阶段能够灵活地利用推理能力。

**关键创新**：论文的关键创新在于提出了动态CoT策略。与传统的CoT方法不同，动态CoT能够根据模型的训练状态和输入数据的特点，自适应地调整CoT数据的使用量，从而避免“过度思考”问题，提高模型的泛化能力。

**关键设计**：动态CoT策略的关键设计在于如何确定何时以及如何注入CoT数据。具体实现细节未知，但推测可能涉及到监控模型在训练过程中的损失函数变化、推理置信度等指标，并根据这些指标动态调整CoT数据的使用比例。损失函数和网络结构等细节未在摘要中提及，属于未知信息。

## 📊 实验亮点

论文通过实验验证了所提出的动态CoT策略在多个MMKP数据集上的有效性。虽然摘要中没有给出具体的性能数据和提升幅度，但强调了实验结果证明了该方法的优越性。具体的性能提升数据需要在论文正文中查找。

## 🎯 应用场景

该研究成果可应用于图像/视频内容理解、智能问答、商品推荐等领域。通过结合视觉信息和文本信息，可以更准确地提取关键短语，从而提升相关应用的性能和用户体验。例如，在电商领域，可以根据商品图片和描述自动生成关键标签，方便用户搜索和浏览。

## 📄 摘要（原文）

> Multi-modal keyphrase prediction (MMKP) aims to advance beyond text-only methods by incorporating multiple modalities of input information to produce a set of conclusive phrases. Traditional multi-modal approaches have been proven to have significant limitations in handling the challenging absence and unseen scenarios. Additionally, we identify shortcomings in existing benchmarks that overestimate model capability due to significant overlap in training tests. In this work, we propose leveraging vision-language models (VLMs) for the MMKP task. Firstly, we use two widely-used strategies, e.g., zero-shot and supervised fine-tuning (SFT) to assess the lower bound performance of VLMs. Next, to improve the complex reasoning capabilities of VLMs, we adopt Fine-tune-CoT, which leverages high-quality CoT reasoning data generated by a teacher model to finetune smaller models. Finally, to address the "overthinking" phenomenon, we propose a dynamic CoT strategy which adaptively injects CoT data during training, allowing the model to flexibly leverage its reasoning capabilities during the inference stage. We evaluate the proposed strategies on various datasets and the experimental results demonstrate the effectiveness of the proposed approaches. The code is available at https://github.com/bytedance/DynamicCoT.

