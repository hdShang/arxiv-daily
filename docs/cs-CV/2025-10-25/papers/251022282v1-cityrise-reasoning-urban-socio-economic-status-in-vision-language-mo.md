---
layout: default
title: CityRiSE: Reasoning Urban Socio-Economic Status in Vision-Language Models via Reinforcement Learning
---

# CityRiSE: Reasoning Urban Socio-Economic Status in Vision-Language Models via Reinforcement Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22282" target="_blank" class="toolbar-btn">arXiv: 2510.22282v1</a>
    <a href="https://arxiv.org/pdf/2510.22282.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22282v1" 
            onclick="toggleFavorite(this, '2510.22282v1', 'CityRiSE: Reasoning Urban Socio-Economic Status in Vision-Language Models via Reinforcement Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tianhui Liu, Hetian Pang, Xin Zhang, Jie Feng, Yong Li, Pan Hui

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-25

---

## 💡 一句话要点

**提出CityRiSE，利用强化学习提升视觉-语言模型在城市社会经济地位推理中的能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `城市社会经济地位` `视觉-语言模型` `强化学习` `多模态学习` `可解释性` `城市规划` `公共政策`

## 📋 核心要点

1. 现有LVLM在视觉数据中进行准确且可解释的社会经济预测方面存在困难，是本文要解决的核心问题。
2. CityRiSE框架通过强化学习引导LVLM关注语义相关的视觉线索，实现结构化和目标导向的社会经济地位推理。
3. 实验表明，CityRiSE显著优于现有基线，提升了预测准确性和在不同城市环境下的泛化能力，尤其是在未见过的城市和指标上。

## 📝 摘要（中文）

本文提出CityRiSE，一个新颖的框架，旨在通过纯强化学习（RL）提升大型视觉-语言模型（LVLMs）在城市社会经济地位推理方面的能力。该框架利用精心策划的多模态数据和可验证的奖励设计，引导LVLM关注语义上有意义的视觉线索，从而实现结构化和目标导向的推理，以进行通用社会经济地位预测。实验结果表明，CityRiSE及其涌现的推理过程显著优于现有的基线方法，提高了预测准确性和跨不同城市环境的泛化能力，尤其是在对未见过的城市和指标进行预测时。这项工作突出了结合强化学习和LVLM在可解释和通用的城市社会经济感知方面的潜力。

## 🔬 方法详解

**问题定义**：现有方法难以让LVLM从视觉数据中进行准确且可解释的社会经济地位预测。LVLM通常难以关注到关键的视觉线索，导致预测结果缺乏可靠性和泛化性。

**核心思路**：CityRiSE的核心思路是利用强化学习，通过奖励机制引导LVLM学习关注与社会经济地位相关的语义信息。通过精心设计的奖励函数，鼓励LVLM进行结构化和目标导向的推理，从而提高预测的准确性和可解释性。

**技术框架**：CityRiSE框架主要包含以下几个模块：1) 多模态数据输入模块，输入街景图像、卫星图像等视觉数据以及相关的文本描述；2) LVLM推理模块，利用LVLM对输入数据进行推理，提取视觉特征和语义信息；3) 强化学习模块，通过奖励函数评估LVLM的推理结果，并利用强化学习算法更新LVLM的参数，使其能够更好地关注关键的视觉线索；4) 社会经济地位预测模块，根据LVLM的推理结果，预测城市社会经济地位。

**关键创新**：CityRiSE的关键创新在于将强化学习引入到LVLM的社会经济地位推理中，通过奖励机制引导LVLM学习关注与社会经济地位相关的语义信息。这种方法能够有效地提高预测的准确性和可解释性，并且具有较强的泛化能力。与现有方法相比，CityRiSE能够更好地利用LVLM的潜力，实现更准确和可解释的社会经济地位预测。

**关键设计**：奖励函数的设计是CityRiSE的关键。奖励函数需要能够准确地评估LVLM的推理结果，并引导LVLM学习关注关键的视觉线索。具体来说，奖励函数可以包括以下几个方面：1) 预测准确度奖励，根据LVLM的预测结果与真实值的差距进行奖励或惩罚；2) 语义一致性奖励，鼓励LVLM关注与社会经济地位相关的语义信息；3) 可解释性奖励，鼓励LVLM生成可解释的推理过程。

## 📊 实验亮点

CityRiSE在城市社会经济地位预测任务上取得了显著的性能提升。实验结果表明，CityRiSE在预测准确性和泛化能力方面均优于现有基线方法，尤其是在对未见过的城市和指标进行预测时，提升幅度明显。具体的数据指标和对比结果在论文中有详细展示。

## 🎯 应用场景

CityRiSE的研究成果可应用于城市规划、公共政策制定、社会经济分析等领域。通过准确预测城市社会经济地位，可以为政府提供决策支持，优化资源配置，促进城市可持续发展。此外，该技术还可以用于商业选址、房地产评估等商业应用，具有广泛的应用前景和实际价值。

## 📄 摘要（原文）

> Harnessing publicly available, large-scale web data, such as street view and satellite imagery, urban socio-economic sensing is of paramount importance for achieving global sustainable development goals. With the emergence of Large Vision-Language Models (LVLMs), new opportunities have arisen to solve this task by treating it as a multi-modal perception and understanding problem. However, recent studies reveal that LVLMs still struggle with accurate and interpretable socio-economic predictions from visual data. To address these limitations and maximize the potential of LVLMs, we introduce \textbf{CityRiSE}, a novel framework for \textbf{R}eason\textbf{i}ng urban \textbf{S}ocio-\textbf{E}conomic status in LVLMs through pure reinforcement learning (RL). With carefully curated multi-modal data and verifiable reward design, our approach guides the LVLM to focus on semantically meaningful visual cues, enabling structured and goal-oriented reasoning for generalist socio-economic status prediction. Experiments demonstrate that CityRiSE with emergent reasoning process significantly outperforms existing baselines, improving both prediction accuracy and generalization across diverse urban contexts, particularly for prediction on unseen cities and unseen indicators. This work highlights the promise of combining RL and LVLMs for interpretable and generalist urban socio-economic sensing.

