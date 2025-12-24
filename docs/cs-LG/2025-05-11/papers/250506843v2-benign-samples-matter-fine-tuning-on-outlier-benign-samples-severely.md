---
layout: default
title: Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety
---

# Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06843" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06843v2</a>
  <a href="https://arxiv.org/pdf/2505.06843.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06843v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06843v2', 'Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Guan, Mengxuan Hu, Ronghang Zhu, Sheng Li, Anil Vullikanti

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-11 (更新: 2025-05-25)

**备注**: 26 pages, 13 figures

**🔗 代码/项目**: [GITHUB](https://github.com/GuanZihan/Benign-Samples-Matter)

---

## 💡 一句话要点

**提出Self-Inf-N以识别良性样本中的异常点，提升LLM安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `异常检测` `微调` `安全性评估` `对齐保障`

## 📋 核心要点

1. 核心问题：现有方法在微调良性样本时，可能导致大型语言模型输出的有害性显著增加，存在安全隐患。
2. 方法要点：本文提出Self-Inf-N，通过异常检测识别良性数据集中对安全性影响最大的样本，进行针对性微调。
3. 实验或效果：在七种主流LLM上进行的实验表明，使用100个异常样本微调后，模型的安全性显著下降，且攻击具有高度可转移性。

## 📝 摘要（中文）

近期研究揭示了大型语言模型（LLMs）在微调阶段的脆弱性：即使在完全良性的训练数据集上微调，也可能显著增加模型输出的有害性。基于这一发现，本文通过开发更有效的攻击方法，分析并识别良性数据集中对安全性降级贡献最大的样本，专门对这些样本进行微调。我们从异常检测的角度出发，提出了Self-Inf-N来检测和提取异常样本。研究表明，使用Self-Inf-N选择的100个异常样本进行微调，严重损害了LLM的安全对齐。通过对七种主流LLM的广泛实验，结果显示该攻击在不同架构间具有高度可转移性，并在实际场景中依然有效。令人担忧的是，现有的大多数缓解策略未能有效防御此攻击，强调了更强大对齐保障的迫切需求。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在微调良性样本时可能导致的安全性降级问题。现有方法未能有效识别和处理良性数据集中潜在的有害样本，导致模型输出的安全性受到威胁。

**核心思路**：论文的核心思路是通过异常检测技术，识别良性数据集中对模型安全性影响最大的样本，并专门对这些样本进行微调，以揭示其对模型输出的潜在危害。这样的设计旨在深入探讨良性样本的潜在风险。

**技术框架**：整体架构包括三个主要模块：首先，使用Self-Inf-N算法进行异常样本的检测和提取；其次，基于提取的异常样本对LLM进行微调；最后，评估微调后模型的安全性和输出质量。

**关键创新**：最重要的技术创新点在于提出了Self-Inf-N算法，该算法能够有效识别良性数据集中的异常样本，与传统方法相比，能够更精准地定位对安全性影响最大的样本。

**关键设计**：在技术细节上，Self-Inf-N算法的参数设置经过精心调整，以确保异常样本的准确识别。同时，微调过程中采用了特定的损失函数，以优化模型在安全性方面的表现。

## 📊 实验亮点

实验结果显示，使用Self-Inf-N选择的100个异常样本进行微调后，七种主流LLM的安全性显著下降，攻击在不同架构间具有高度可转移性。大多数现有的缓解策略未能有效防御此攻击，强调了对齐保障的迫切需求。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全性评估和改进，尤其是在对抗性攻击和安全对齐方面。通过识别和处理良性样本中的异常点，可以为模型的安全性提供更强的保障，减少有害输出的风险。未来，这一方法可能在多个领域中得到广泛应用，如自然语言处理、自动化客服和内容生成等。

## 📄 摘要（原文）

> Recent studies have uncovered a troubling vulnerability in the fine-tuning stage of large language models (LLMs): even fine-tuning on entirely benign datasets can lead to a significant increase in the harmfulness of LLM outputs. Building on this finding, our red teaming study takes this threat one step further by developing a more effective attack. Specifically, we analyze and identify samples within benign datasets that contribute most to safety degradation, then fine-tune LLMs exclusively on these samples. We approach this problem from an outlier detection perspective and propose Self-Inf-N, to detect and extract outliers for fine-tuning. Our findings reveal that fine-tuning LLMs on 100 outlier samples selected by Self-Inf-N in the benign datasets severely compromises LLM safety alignment. Extensive experiments across seven mainstream LLMs demonstrate that our attack exhibits high transferability across different architectures and remains effective in practical scenarios. Alarmingly, our results indicate that most existing mitigation strategies fail to defend against this attack, underscoring the urgent need for more robust alignment safeguards. Codes are available at https://github.com/GuanZihan/Benign-Samples-Matter.

