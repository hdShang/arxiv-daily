---
layout: default
title: GraphTracer: Graph-Guided Failure Tracing in LLM Agents for Robust Multi-Turn Deep Search
---

# GraphTracer: Graph-Guided Failure Tracing in LLM Agents for Robust Multi-Turn Deep Search

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.10581" target="_blank" class="toolbar-btn">arXiv: 2510.10581v1</a>
    <a href="https://arxiv.org/pdf/2510.10581.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10581v1" 
            onclick="toggleFavorite(this, '2510.10581v1', 'GraphTracer: Graph-Guided Failure Tracing in LLM Agents for Robust Multi-Turn Deep Search')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Heng Zhang, Yuling Shi, Xiaodong Gu, Haochen You, Zijian Zhang, Lubin Gan, Yilei Yuan, Jin Huang

**分类**: cs.GR

**发布日期**: 2025-10-12

---

## 💡 一句话要点

**GraphTracer：基于图引导的LLM Agent故障追踪，提升多轮深度搜索的鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多Agent系统` `故障追踪` `信息依赖图` `LLM Agent` `深度搜索`

## 📋 核心要点

1. 多Agent系统在复杂任务中易失败，现有方法难以有效追踪跨Agent的错误传播和信息依赖。
2. GraphTracer通过构建信息依赖图（IDG）来显式捕获Agent间的信息流，从而定位根本原因。
3. 实验表明，GraphTracer在归因准确率上提升高达18.18%，并在实际部署中带来显著的性能提升。

## 📝 摘要（中文）

大型语言模型驱动的多Agent系统在复杂任务中表现出色，但多轮深度搜索场景下的失败率很高。现有的时序归因方法难以准确诊断根本原因，尤其是在错误跨多个Agent传播时。通过分析动作序列来自动化故障归因的方法，由于无法考虑跨Agent的信息依赖关系而效果不佳。本文提出了两个核心挑战：(i)区分多Agent错误传播中的症状和根本原因，以及(ii)追踪超越时序的信息依赖关系。为了解决这些问题，我们引入了GraphTracer，一个通过信息流分析重新定义故障归因的框架。GraphTracer构建信息依赖图(IDG)来显式地捕获Agent如何引用和构建先前的输出。它通过追踪这些依赖结构而不是依赖于时序来定位根本原因。GraphTracer还使用图感知的合成数据生成来针对关键节点，创建真实的失败场景。在Who&When基准测试和生产系统中的集成评估表明，GraphTracer-8B实现了比最先进模型高出18.18%的归因准确率，并在部署的多Agent框架中实现了4.8%到14.2%的性能提升，为多Agent系统调试建立了一个强大的解决方案。

## 🔬 方法详解

**问题定义**：多Agent系统在多轮深度搜索任务中容易失败，现有方法如时序归因和动作序列分析无法有效追踪跨Agent的错误传播，难以区分症状和根本原因，导致故障诊断不准确。现有方法忽略了Agent之间的信息依赖关系，无法定位到真正的错误源头。

**核心思路**：GraphTracer的核心思路是通过构建信息依赖图（IDG）来显式地建模Agent之间的信息依赖关系。通过分析信息在Agent之间的流动和传递，可以更准确地定位到导致最终失败的根本原因，而不是仅仅关注表面的错误症状。这种方法避免了仅依赖时序信息的局限性。

**技术框架**：GraphTracer框架主要包含以下几个阶段：1) 构建信息依赖图（IDG）：分析Agent之间的交互过程，提取Agent之间的信息依赖关系，构建IDG。IDG的节点代表Agent的输出，边代表Agent之间的信息依赖关系。2) 故障追踪：通过在IDG上进行追踪，从最终的失败结果出发，沿着信息依赖关系反向追踪，定位到导致失败的根本原因。3) 图感知的合成数据生成：针对IDG中的关键节点，生成具有代表性的合成数据，用于训练和评估故障追踪模型。

**关键创新**：GraphTracer的关键创新在于将信息流分析引入到多Agent系统的故障追踪中。与传统的时序分析方法不同，GraphTracer关注Agent之间的信息依赖关系，能够更准确地定位到导致失败的根本原因。此外，图感知的合成数据生成方法能够有效地针对关键节点生成数据，提高模型的鲁棒性。

**关键设计**：IDG的构建是GraphTracer的关键。IDG的节点表示Agent的输出，边表示Agent之间的信息依赖关系。边的权重可以根据信息依赖的强度进行调整。故障追踪算法采用图搜索算法，例如深度优先搜索或广度优先搜索，沿着信息依赖关系反向追踪。图感知的合成数据生成方法需要根据IDG的结构和节点的重要性来设计生成策略。

## 📊 实验亮点

GraphTracer-8B在Who&When基准测试中，相比于最先进的模型，实现了高达18.18%的归因准确率提升。在实际部署的多Agent框架中，GraphTracer带来了4.8%到14.2%的性能提升。这些结果表明GraphTracer能够有效地提高多Agent系统的鲁棒性和可靠性。

## 🎯 应用场景

GraphTracer可应用于各种基于LLM的复杂多Agent系统，例如智能客服、自动化流程管理、协同设计等。通过提高系统的稳定性和可靠性，降低维护成本，提升用户体验。未来可扩展到更复杂的Agent交互模式和更广泛的应用领域，例如机器人协作、自动驾驶等。

## 📄 摘要（原文）

> Multi-agent systems powered by Large Language Models excel at complex tasks through coordinated collaboration, yet they face high failure rates in multi-turn deep search scenarios. Existing temporal attribution methods struggle to accurately diagnose root causes, particularly when errors propagate across multiple agents. Attempts to automate failure attribution by analyzing action sequences remain ineffective due to their inability to account for information dependencies that span agents. This paper identifies two core challenges: \textit{(i) distinguishing symptoms from root causes in multi-agent error propagation}, and \textit{(ii) tracing information dependencies beyond temporal order}. To address these issues, we introduce \textbf{GraphTracer}, a framework that redefines failure attribution through information flow analysis. GraphTracer constructs Information Dependency Graphs (IDGs) to explicitly capture how agents reference and build on prior outputs. It localizes root causes by tracing through these dependency structures instead of relying on temporal sequences. GraphTracer also uses graph-aware synthetic data generation to target critical nodes, creating realistic failure scenarios. Evaluations on the Who\&When benchmark and integration into production systems demonstrate that GraphTracer-8B achieves up to 18.18\% higher attribution accuracy compared to state-of-the-art models and enables 4.8\% to 14.2\% performance improvements in deployed multi-agent frameworks, establishing a robust solution for multi-agent system debugging.

