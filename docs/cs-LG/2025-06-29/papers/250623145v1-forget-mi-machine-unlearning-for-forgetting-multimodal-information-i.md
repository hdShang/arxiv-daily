---
layout: default
title: "Forget-MI: Machine Unlearning for Forgetting Multimodal Information in Healthcare Settings"
---

# Forget-MI: Machine Unlearning for Forgetting Multimodal Information in Healthcare Settings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23145" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23145v1</a>
  <a href="https://arxiv.org/pdf/2506.23145.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23145v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23145v1', 'Forget-MI: Machine Unlearning for Forgetting Multimodal Information in Healthcare Settings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shahad Hardan, Darya Taratynova, Abdelmajid Essofi, Karthik Nandakumar, Mohammad Yaqub

**分类**: cs.LG, cs.CR, cs.CV

**发布日期**: 2025-06-29

**🔗 代码/项目**: [GITHUB](https://github.com/BioMedIA-MBZUAI/Forget-MI.git)

---

## 💡 一句话要点

**提出Forget-MI以解决医疗领域多模态信息遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器遗忘` `多模态数据` `隐私保护` `医疗AI` `成员推断攻击` `模型评估` `损失函数` `扰动技术`

## 📋 核心要点

1. 现有的机器遗忘方法在医疗领域的多模态架构中难以有效移除患者数据，影响隐私保护。
2. Forget-MI通过设计新的损失函数和扰动技术，实现对多模态医疗数据的有效遗忘，同时保持模型性能。
3. 实验结果显示，Forget-MI在减少MIA方面表现优异，遗忘数据集的AUC和F1分数显著降低，同时测试集性能与重训练模型相当。

## 📝 摘要（中文）

在人工智能中，隐私保护至关重要，尤其是在医疗领域，模型依赖于敏感的患者数据。在新兴的机器遗忘领域，现有方法难以从训练好的多模态架构中移除患者数据。我们提出了Forget-MI，一种针对多模态医疗数据的新型机器遗忘方法，通过建立损失函数和扰动技术来实现。该方法能够遗忘请求遗忘的数据的单模态和联合表示，同时保留剩余数据的知识，并保持与原始模型相当的性能。我们通过对遗忘数据集的性能、测试数据集的性能以及衡量攻击者区分遗忘数据集与训练数据集能力的成员推断攻击（MIA）进行评估。我们的模型在减少MIA和遗忘数据集性能方面优于现有方法，同时在测试集上的性能保持一致。

## 🔬 方法详解

**问题定义**：本论文旨在解决在医疗领域中，现有机器遗忘方法无法有效从多模态模型中移除患者数据的问题。这导致了隐私保护的挑战，尤其是在处理敏感信息时。

**核心思路**：Forget-MI的核心思路是通过建立新的损失函数和扰动技术，针对请求遗忘的数据进行有效的遗忘操作，同时保留其他数据的知识，以确保模型性能不受显著影响。

**技术框架**：该方法的整体架构包括数据预处理、损失函数设计、扰动技术应用和模型评估四个主要模块。首先对数据进行分类，然后应用特定的损失函数进行训练，最后通过评估指标验证模型性能。

**关键创新**：Forget-MI的主要创新在于其能够同时处理单模态和联合表示的遗忘需求，并且在保持模型性能的同时，显著降低了MIA的风险。这与现有方法的单一模态处理方式形成了鲜明对比。

**关键设计**：在关键设计方面，Forget-MI引入了特定的损失函数来平衡遗忘与知识保留，并采用扰动技术来增强模型的鲁棒性。具体参数设置和网络结构的细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，Forget-MI在减少MIA方面表现优异，具体减少幅度为0.202，同时在遗忘数据集上的AUC和F1分数分别降低了0.221和0.305。值得注意的是，测试集的性能与重训练模型相当，显示出该方法在遗忘能力与性能保持之间的良好平衡。

## 🎯 应用场景

该研究的潜在应用领域主要集中在医疗数据处理和隐私保护方面。随着对患者隐私的重视，Forget-MI可以帮助医疗机构在处理敏感数据时，确保在必要时有效地遗忘特定信息，从而提升患者信任度和数据安全性。未来，该方法也可扩展至其他需要隐私保护的领域，如金融和社交媒体。

## 📄 摘要（原文）

> Privacy preservation in AI is crucial, especially in healthcare, where models rely on sensitive patient data. In the emerging field of machine unlearning, existing methodologies struggle to remove patient data from trained multimodal architectures, which are widely used in healthcare. We propose Forget-MI, a novel machine unlearning method for multimodal medical data, by establishing loss functions and perturbation techniques. Our approach unlearns unimodal and joint representations of the data requested to be forgotten while preserving knowledge from the remaining data and maintaining comparable performance to the original model. We evaluate our results using performance on the forget dataset, performance on the test dataset, and Membership Inference Attack (MIA), which measures the attacker's ability to distinguish the forget dataset from the training dataset. Our model outperforms the existing approaches that aim to reduce MIA and the performance on the forget dataset while keeping an equivalent performance on the test set. Specifically, our approach reduces MIA by 0.202 and decreases AUC and F1 scores on the forget set by 0.221 and 0.305, respectively. Additionally, our performance on the test set matches that of the retrained model, while allowing forgetting. Code is available at https://github.com/BioMedIA-MBZUAI/Forget-MI.git

