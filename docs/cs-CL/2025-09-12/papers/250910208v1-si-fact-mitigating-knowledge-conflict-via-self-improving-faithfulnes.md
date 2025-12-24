---
layout: default
title: "SI-FACT: Mitigating Knowledge Conflict via Self-Improving Faithfulness-Aware Contrastive Tuning"
---

# SI-FACT: Mitigating Knowledge Conflict via Self-Improving Faithfulness-Aware Contrastive Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10208" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10208v1</a>
  <a href="https://arxiv.org/pdf/2509.10208.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10208v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10208v1', 'SI-FACT: Mitigating Knowledge Conflict via Self-Improving Faithfulness-Aware Contrastive Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengqiang Fu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**提出SI-FACT框架，通过自提升的忠实度感知对比学习缓解LLM的知识冲突问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `知识冲突` `对比学习` `自指令学习` `上下文忠实度`

## 📋 核心要点

1. 大型语言模型在知识密集型任务中面临知识冲突问题，即模型倾向于使用内部知识而非给定的上下文。
2. SI-FACT框架利用自指令机制自动生成对比学习数据，包括正负样本，降低了人工标注成本。
3. 实验结果表明，SI-FACT在上下文召回率上优于现有方法，并降低了模型对内部记忆的依赖。

## 📝 摘要（中文）

大型语言模型在知识密集型任务中，由于知识冲突，经常产生不忠实的回应，即倾向于依赖内部参数知识而非提供的上下文。为了解决这个问题，我们提出了一种新颖的自提升框架，即自提升忠实度感知对比学习（SI-FACT）。该框架使用自指令机制，允许基础LLM自动生成高质量、结构化的对比学习数据，包括锚样本、语义等价的正样本和模拟不忠实场景的负样本。这种方法显著降低了手动标注的成本。随后，应用对比学习来训练模型，使其在表征空间中拉近忠实回应，推远不忠实回应。在知识冲突评估基准ECARE KRE和COSE KRE上的实验表明，基于Llama3 8B Instruct的SI-FACT模型比最佳基线方法提高了6.2%的上下文召回率，同时显著降低了对内部记忆的依赖。结果表明，SI-FACT在增强LLM的上下文忠实度方面提供了强大的有效性和高数据效率，为构建更主动和值得信赖的语言模型提供了一条实用的途径。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在知识密集型任务中出现的知识冲突问题。现有方法的痛点在于，LLM倾向于依赖其内部参数知识，而忽略或错误地利用提供的上下文信息，导致生成不忠实的回应。这种现象降低了LLM在需要精确知识的任务中的可靠性。

**核心思路**：论文的核心思路是利用对比学习，通过拉近忠实回应的表征，推远不忠实回应的表征，从而使模型更加关注上下文信息。为了降低数据标注成本，论文采用自指令机制，让LLM自动生成对比学习所需的数据。

**技术框架**：SI-FACT框架主要包含两个阶段：数据生成阶段和对比学习训练阶段。在数据生成阶段，利用自指令机制，通过设计特定的prompt，让LLM生成锚样本、语义等价的正样本以及模拟不忠实场景的负样本。在对比学习训练阶段，使用生成的数据训练模型，通过对比损失函数，使模型学习到区分忠实和不忠实回应的表征。

**关键创新**：该论文的关键创新在于提出了一种自提升的框架，能够自动生成高质量的对比学习数据，从而避免了昂贵的人工标注。此外，论文还设计了特定的prompt，用于生成模拟不忠实场景的负样本，从而使模型能够更好地识别和避免知识冲突。

**关键设计**：在数据生成阶段，设计了不同的prompt模板，用于生成不同类型的样本。例如，对于负样本的生成，prompt会引导模型忽略或错误地使用上下文信息。在对比学习训练阶段，使用了InfoNCE损失函数，该损失函数能够有效地拉近正样本的表征，推远负样本的表征。具体的参数设置和网络结构细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

实验结果表明，基于Llama3 8B Instruct的SI-FACT模型在ECARE KRE和COSE KRE两个知识冲突评估基准上，比最佳基线方法提高了6.2%的上下文召回率。同时，SI-FACT模型显著降低了对内部记忆的依赖，表明其在增强LLM的上下文忠实度方面具有强大的有效性和高数据效率。

## 🎯 应用场景

该研究成果可应用于各种知识密集型任务，例如问答系统、信息检索和文本摘要等。通过提高语言模型的上下文忠实度，可以显著提升这些应用在实际场景中的可靠性和准确性。未来，该方法可以进一步扩展到其他类型的语言模型和任务中，从而构建更加值得信赖的人工智能系统。

## 📄 摘要（原文）

> Large Language Models often generate unfaithful responses in knowledge intensive tasks due to knowledge conflict,that is,a preference for relying on internal parametric knowledge rather than the provided context.To address this issue,we propose a novel self improving framework,Self Improving Faithfulness Aware Contrastive Tuning.The framework uses a self instruct mechanism that allows the base LLM to automatically generate high quality,structured contrastive learning data,including anchor samples,semantically equivalent positive samples,and negative samples simulating unfaithful scenarios.This approach significantly reduces the cost of manual annotation.Subsequently,contrastive learning is applied to train the model,enabling it to pull faithful responses closer and push unfaithful responses farther apart in the representation space.Experiments on knowledge conflict evaluation benchmarks ECARE KRE and COSE KRE show that the SI FACT model based on Llama3 8B Instruct improves the Contextual Recall Rate by 6.2% over the best baseline method,while significantly reducing dependence on internal memory.The results indicate that SI FACT provides strong effectiveness and high data efficiency in enhancing the contextual faithfulness of LLMs,offering a practical pathway toward building more proactive and trustworthy language models.

