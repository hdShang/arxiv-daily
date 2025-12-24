---
layout: default
title: A new membership inference attack that spots memorization in generative and predictive models: Loss-Based with Reference Model algorithm (LBRM)
---

# A new membership inference attack that spots memorization in generative and predictive models: Loss-Based with Reference Model algorithm (LBRM)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03490" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03490v1</a>
  <a href="https://arxiv.org/pdf/2505.03490.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03490v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03490v1', 'A new membership inference attack that spots memorization in generative and predictive models: Loss-Based with Reference Model algorithm (LBRM)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Faiz Taleb, Ivan Gazeau, Maryline Laurent

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出LBRM算法以解决生成模型中的记忆化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `生成模型` `隐私保护` `成员推断` `时间序列插补` `损失函数` `参考模型` `机器学习`

## 📋 核心要点

1. 现有生成模型在训练过程中可能会无意中记忆训练数据，导致隐私泄露风险。
2. 本文提出的LBRM算法通过参考模型来增强成员推断攻击的准确性，能够有效区分训练和测试数据。
3. 实验结果表明，LBRM算法在未调优和调优情况下，AUROC分别提升约40%和60%，显示出其优越性。

## 📝 摘要（中文）

生成模型可能无意中记忆训练数据，从而带来显著的隐私风险。本文针对时间序列插补模型中的记忆现象，提出了基于损失的参考模型算法（LBRM）。该方法利用参考模型提高了成员推断攻击的准确性，能够有效区分训练数据和测试数据。我们的贡献主要体现在两个方面：首先，提出了一种创新的方法来有效提取和识别记忆的训练数据，检测准确性显著提高，未调优情况下AUROC平均提升约40%，调优后AUROC提升约60%。其次，我们通过对两种时间序列插补架构的成员推断攻击验证了该方法的鲁棒性和多样性，强调了LBRM在提高检测准确性方面的重要性，解决了时间序列插补模型中的隐私风险。

## 🔬 方法详解

**问题定义**：本文旨在解决生成模型中训练数据的记忆化问题，现有方法在识别记忆数据时准确性不足，无法有效保护隐私。

**核心思路**：LBRM算法通过引入参考模型，增强了成员推断攻击的准确性，能够更好地区分训练数据和测试数据，从而有效识别记忆数据。

**技术框架**：LBRM算法的整体架构包括数据预处理、参考模型构建、损失计算和成员推断四个主要模块。首先对输入数据进行预处理，然后构建参考模型以获取基准损失，接着计算目标模型的损失，并通过比较来进行成员推断。

**关键创新**：LBRM算法的核心创新在于利用参考模型来提升成员推断攻击的准确性，这一设计与传统方法相比，显著提高了对记忆数据的识别能力。

**关键设计**：在算法实现中，关键参数包括参考模型的选择、损失函数的设计以及网络结构的优化。通过合理设置这些参数，LBRM算法能够在不同的时间序列插补架构中保持高效的性能。

## 📊 实验亮点

实验结果显示，LBRM算法在未调优情况下AUROC平均提升约40%，而在调优后AUROC提升约60%。这些数据表明，LBRM算法在成员推断攻击中的表现显著优于传统方法，展现出其在不同架构下的鲁棒性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括数据隐私保护、金融预测、医疗数据分析等。通过提高生成模型的隐私保护能力，LBRM算法能够在实际应用中有效防止敏感信息泄露，具有重要的社会价值和实际意义。未来，该方法可能会推动更多隐私保护技术的发展，促进生成模型在各领域的安全应用。

## 📄 摘要（原文）

> Generative models can unintentionally memorize training data, posing significant privacy risks. This paper addresses the memorization phenomenon in time series imputation models, introducing the Loss-Based with Reference Model (LBRM) algorithm. The LBRM method leverages a reference model to enhance the accuracy of membership inference attacks, distinguishing between training and test data. Our contributions are twofold: first, we propose an innovative method to effectively extract and identify memorized training data, significantly improving detection accuracy. On average, without fine-tuning, the AUROC improved by approximately 40\%. With fine-tuning, the AUROC increased by approximately 60\%. Second, we validate our approach through membership inference attacks on two types of architectures designed for time series imputation, demonstrating the robustness and versatility of the LBRM approach in different contexts. These results highlight the significant enhancement in detection accuracy provided by the LBRM approach, addressing privacy risks in time series imputation models.

