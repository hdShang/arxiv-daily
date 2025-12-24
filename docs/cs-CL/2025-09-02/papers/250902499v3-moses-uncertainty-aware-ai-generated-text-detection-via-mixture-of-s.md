---
layout: default
title: "MoSEs: Uncertainty-Aware AI-Generated Text Detection via Mixture of Stylistics Experts with Conditional Thresholds"
---

# MoSEs: Uncertainty-Aware AI-Generated Text Detection via Mixture of Stylistics Experts with Conditional Thresholds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02499" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02499v3</a>
  <a href="https://arxiv.org/pdf/2509.02499.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02499v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02499v3', 'MoSEs: Uncertainty-Aware AI-Generated Text Detection via Mixture of Stylistics Experts with Conditional Thresholds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junxi Wu, Jinpeng Wang, Zheng Liu, Bin Chen, Dongjian Hu, Hao Wu, Shu-Tao Xia

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-02 (更新: 2025-09-08)

**备注**: EMNLP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/creator-xi/MoSEs)

---

## 💡 一句话要点

**MoSEs：基于风格专家混合与条件阈值的不确定性感知AI生成文本检测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI生成文本检测` `风格建模` `不确定性量化` `条件阈值估计` `低资源学习`

## 📋 核心要点

1. 现有AI生成文本检测方法忽略文本风格，依赖静态阈值，导致检测性能受限。
2. MoSEs框架通过风格专家混合和条件阈值估计，实现风格感知的AI生成文本检测。
3. 实验表明，MoSEs相比基线方法平均提升11.34%的检测性能，在低资源场景下提升高达39.15%。

## 📝 摘要（中文）

大型语言模型的快速发展加剧了公众对其潜在滥用的担忧。因此，构建可信赖的AI生成文本检测系统至关重要。现有方法忽略了风格建模，并且主要依赖于静态阈值，这极大地限制了检测性能。本文提出了风格专家混合（MoSEs）框架，该框架通过条件阈值估计实现风格感知的不确定性量化。MoSEs包含三个核心组件，即风格参考库（SRR）、风格感知路由器（SAR）和条件阈值估计器（CTE）。对于输入文本，SRR可以激活SRR中适当的参考数据，并将其提供给CTE。随后，CTE联合建模语言统计属性和语义特征，以动态确定最佳阈值。通过判别分数，MoSEs产生具有相应置信水平的预测标签。与基线方法相比，我们的框架在检测性能方面平均提高了11.34%。更令人鼓舞的是，MoSEs在低资源情况下表现出更明显的改进，达到了39.15%。我们的代码可在https://github.com/creator-xi/MoSEs上找到。

## 🔬 方法详解

**问题定义**：现有AI生成文本检测方法在区分人类撰写和AI生成文本时，未能充分考虑文本的风格特征。它们通常依赖于固定的阈值来判断文本的真伪，这使得它们难以适应不同风格的AI生成文本，尤其是在低资源场景下，检测性能会显著下降。

**核心思路**：MoSEs的核心思路是利用风格信息来提高AI生成文本检测的准确性和鲁棒性。它通过构建一个风格参考库，并根据输入文本的风格动态地调整检测阈值，从而实现风格感知的AI生成文本检测。这种方法能够更好地适应不同风格的AI生成文本，并提高在低资源场景下的检测性能。

**技术框架**：MoSEs框架包含三个主要组件：风格参考库（SRR）、风格感知路由器（SAR）和条件阈值估计器（CTE）。首先，SRR存储了各种风格的文本数据。当输入一段文本时，SAR会根据其风格特征从SRR中选择最相关的参考数据。然后，CTE会利用这些参考数据，结合输入文本的语言统计属性和语义特征，动态地估计一个最优的检测阈值。最后，根据判别分数和动态阈值，MoSEs输出预测标签和相应的置信度。

**关键创新**：MoSEs的关键创新在于其风格感知的阈值估计方法。与传统的静态阈值方法不同，MoSEs能够根据输入文本的风格动态地调整检测阈值，从而更好地适应不同风格的AI生成文本。此外，MoSEs还引入了风格参考库，用于存储各种风格的文本数据，这为风格感知的阈值估计提供了基础。

**关键设计**：SRR的设计需要考虑如何有效地存储和检索不同风格的文本数据。SAR的设计需要考虑如何准确地识别输入文本的风格特征，并选择最相关的参考数据。CTE的设计需要考虑如何有效地结合语言统计属性、语义特征和参考数据，以动态地估计一个最优的检测阈值。具体的参数设置、损失函数和网络结构等技术细节在论文中进行了详细描述。

## 📊 实验亮点

MoSEs在AI生成文本检测任务上取得了显著的性能提升。与基线方法相比，平均检测性能提升了11.34%。更值得关注的是，在低资源场景下，MoSEs的性能提升高达39.15%，表明其在数据稀缺的情况下具有更强的鲁棒性。这些实验结果充分验证了MoSEs框架的有效性和优越性。

## 🎯 应用场景

MoSEs技术可应用于内容安全、学术诚信、舆情分析等领域。通过准确识别AI生成的文本，可以有效防止虚假信息的传播，维护网络空间的健康秩序。该技术还有助于检测学术论文中的抄袭行为，保障学术研究的原创性。未来，MoSEs有望成为构建可信AI生态的重要组成部分。

## 📄 摘要（原文）

> The rapid advancement of large language models has intensified public concerns about the potential misuse. Therefore, it is important to build trustworthy AI-generated text detection systems. Existing methods neglect stylistic modeling and mostly rely on static thresholds, which greatly limits the detection performance. In this paper, we propose the Mixture of Stylistic Experts (MoSEs) framework that enables stylistics-aware uncertainty quantification through conditional threshold estimation. MoSEs contain three core components, namely, the Stylistics Reference Repository (SRR), the Stylistics-Aware Router (SAR), and the Conditional Threshold Estimator (CTE). For input text, SRR can activate the appropriate reference data in SRR and provide them to CTE. Subsequently, CTE jointly models the linguistic statistical properties and semantic features to dynamically determine the optimal threshold. With a discrimination score, MoSEs yields prediction labels with the corresponding confidence level. Our framework achieves an average improvement 11.34% in detection performance compared to baselines. More inspiringly, MoSEs shows a more evident improvement 39.15% in the low-resource case. Our code is available at https://github.com/creator-xi/MoSEs.

