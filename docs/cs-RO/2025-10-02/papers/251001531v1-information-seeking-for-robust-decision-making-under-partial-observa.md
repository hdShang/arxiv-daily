---
layout: default
title: Information Seeking for Robust Decision Making under Partial Observability
---

# Information Seeking for Robust Decision Making under Partial Observability

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.01531" target="_blank" class="toolbar-btn">arXiv: 2510.01531v1</a>
    <a href="https://arxiv.org/pdf/2510.01531.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01531v1" 
            onclick="toggleFavorite(this, '2510.01531v1', 'Information Seeking for Robust Decision Making under Partial Observability')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Djengo Cyun-Jyun Fang, Tsung-Wei Ke

**分类**: cs.AI, cs.CL, cs.RO

**发布日期**: 2025-10-02

**备注**: The project page is available at https://infoseekerllm.github.io

---

## 💡 一句话要点

**InfoSeeker：结合信息搜寻的LLM决策框架，提升部分可观测环境下的决策鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `信息搜寻` `决策规划` `部分可观测性` `机器人操作`

## 📋 核心要点

1. 现有LLM智能体在部分可观测环境中决策时，忽略了内部动态与实际环境的差异，导致决策鲁棒性不足。
2. InfoSeeker框架通过集成任务导向规划和信息搜寻，主动验证理解、检测变化和测试假设，从而校准内部动态。
3. 实验表明，InfoSeeker在部分可观测环境中显著提升了性能，并在机器人操作和Web导航等任务中优于基线。

## 📝 摘要（中文）

在信息不完整和动态环境噪声干扰的实际环境中，主动信息搜寻对于人类解决问题至关重要。当无法直接观察到真实环境状态时，人类会通过搜寻信息来更新其内部动态，并为未来的决策提供依据。虽然现有的大型语言模型（LLM）规划智能体已经处理了观测不确定性，但它们常常忽略自身内部动态与实际环境之间的差异。本文提出了一种名为信息搜寻决策规划器（InfoSeeker）的LLM决策框架，该框架将面向任务的规划与信息搜寻相结合，以校准内部动态，并在智能体观测和环境动态均存在不确定性的情况下做出最优决策。InfoSeeker提示LLM主动收集信息，通过规划行动来验证其理解、检测环境变化或在生成或修改面向任务的计划之前测试假设。为了评估InfoSeeker，本文引入了一个新的基准测试套件，该套件包含具有不完整观测和不确定动态的部分可观测环境。实验表明，InfoSeeker在不牺牲样本效率的情况下，比现有方法实现了74%的绝对性能提升。此外，InfoSeeker可以推广到不同的LLM，并且在机器人操作和Web导航等已建立的基准测试中优于基线方法。这些发现强调了紧密集成规划和信息搜寻对于在部分可观测环境中实现鲁棒行为的重要性。

## 🔬 方法详解

**问题定义**：论文旨在解决部分可观测环境下，LLM智能体由于内部状态与真实环境不一致而导致的决策鲁棒性问题。现有方法通常只关注观测的不确定性，而忽略了环境动态变化带来的影响，导致智能体无法及时调整策略，做出最优决策。

**核心思路**：InfoSeeker的核心思路是将信息搜寻与任务规划紧密结合。智能体在执行任务前，会主动规划信息搜寻动作，通过观察环境变化、验证自身理解来校准内部状态，从而更好地适应真实环境，做出更明智的决策。这种主动的信息获取机制能够有效减少内部状态与环境之间的偏差。

**技术框架**：InfoSeeker框架主要包含以下几个阶段：1) **初始规划**：LLM根据初始状态和任务目标生成初步的任务规划。2) **信息搜寻规划**：LLM根据当前状态和任务规划，生成信息搜寻动作，例如观察特定区域、询问特定问题等。3) **执行与观察**：执行信息搜寻动作，并观察环境反馈。4) **状态更新**：根据观察结果更新内部状态，包括环境模型和任务规划。5) **迭代优化**：重复上述过程，直到任务完成或达到预设的迭代次数。

**关键创新**：InfoSeeker的关键创新在于将信息搜寻作为决策过程中的一个主动环节，而不是被动地接受观测。通过主动的信息搜寻，智能体可以更好地理解环境动态，验证自身假设，从而提高决策的鲁棒性。与现有方法相比，InfoSeeker更加注重内部状态与环境的对齐，能够更好地适应复杂多变的环境。

**关键设计**：InfoSeeker使用LLM作为核心决策引擎，通过精心设计的Prompt来引导LLM进行任务规划和信息搜寻。Prompt的设计需要考虑以下几个方面：1) **任务描述**：清晰地描述任务目标和约束条件。2) **状态信息**：提供当前环境状态的描述，包括观测信息和内部状态。3) **行动空间**：定义可执行的动作集合，包括任务相关动作和信息搜寻动作。4) **奖励函数**：定义任务完成的奖励和信息搜寻的成本。通过优化Prompt设计，可以有效地提高LLM的决策能力和信息搜寻效率。

## 📊 实验亮点

实验结果表明，InfoSeeker在部分可观测环境中取得了显著的性能提升，相比现有方法，绝对性能提升了74%。此外，InfoSeeker在机器人操作和Web导航等已建立的基准测试中也优于基线方法，证明了其泛化能力。更重要的是，InfoSeeker在不牺牲样本效率的前提下实现了性能提升，表明其具有较高的实用价值。

## 🎯 应用场景

InfoSeeker框架具有广泛的应用前景，例如机器人导航、智能家居、自动驾驶、金融交易等领域。在这些领域中，环境通常是部分可观测的，并且存在动态变化。InfoSeeker可以通过主动信息搜寻来提高决策的鲁棒性，从而实现更安全、更可靠的智能系统。未来，该框架还可以扩展到多智能体协作等更复杂的场景。

## 📄 摘要（原文）

> Explicit information seeking is essential to human problem-solving in practical environments characterized by incomplete information and noisy dynamics. When the true environmental state is not directly observable, humans seek information to update their internal dynamics and inform future decision-making. Although existing Large Language Model (LLM) planning agents have addressed observational uncertainty, they often overlook discrepancies between their internal dynamics and the actual environment. We introduce Information Seeking Decision Planner (InfoSeeker), an LLM decision-making framework that integrates task-oriented planning with information seeking to align internal dynamics and make optimal decisions under uncertainty in both agent observations and environmental dynamics. InfoSeeker prompts an LLM to actively gather information by planning actions to validate its understanding, detect environmental changes, or test hypotheses before generating or revising task-oriented plans. To evaluate InfoSeeker, we introduce a novel benchmark suite featuring partially observable environments with incomplete observations and uncertain dynamics. Experiments demonstrate that InfoSeeker achieves a 74% absolute performance gain over prior methods without sacrificing sample efficiency. Moreover, InfoSeeker generalizes across LLMs and outperforms baselines on established benchmarks such as robotic manipulation and web navigation. These findings underscore the importance of tightly integrating planning and information seeking for robust behavior in partially observable environments. The project page is available at https://infoseekerllm.github.io

