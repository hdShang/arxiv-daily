---
layout: default
title: "LLM Hallucination Detection: HSAD"
---

# LLM Hallucination Detection: HSAD

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23580" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23580v2</a>
  <a href="https://arxiv.org/pdf/2509.23580.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23580v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23580v2', 'LLM Hallucination Detection: HSAD')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: JinXin Li, Gang Tu, JunJie Hu

**分类**: cs.CL

**发布日期**: 2025-09-28 (更新: 2025-10-08)

**备注**: in Chinese language

---

## 💡 一句话要点

**提出HSAD，通过频域分析LLM隐藏层信号以检测幻觉**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `幻觉检测` `频域分析` `隐藏层信号` `快速傅里叶变换`

## 📋 核心要点

1. 现有幻觉检测方法依赖知识覆盖范围有限的事实一致性验证，或难以捕捉推理偏差的静态隐藏层特征。
2. HSAD将LLM推理视为认知过程，通过隐藏层时域信号模拟人类信号感知，并进行频域分析。
3. 实验表明，HSAD通过频域特征有效捕捉推理异常，提升了幻觉检测的准确性和鲁棒性。

## 📝 摘要（中文）

大型语言模型（LLM）在语言理解和代码生成等任务中表现出强大的能力，但生成过程中频繁出现的幻觉严重阻碍了它们在关键应用场景中的部署。目前主流的幻觉检测方法依赖于事实一致性验证或静态隐藏层特征，前者受知识覆盖范围的限制，后者难以捕捉推理过程中的偏差。为了解决这些问题，受认知神经科学中信号分析方法的启发，本文提出了一种基于隐藏层时域信号频域分析的幻觉检测方法，名为HSAD（基于隐藏信号分析的检测）。该方法将LLM的推理过程视为随时间展开的认知过程，通过隐藏层时域信号来模拟人类在欺骗检测场景中的信号感知和辨别过程。然后，应用快速傅里叶变换将这些时域信号映射到频域，构建频谱特征，用于捕捉推理过程中出现的异常。对这些频谱特征的分析实验证明了该方法的有效性。最后，设计了一种基于这些频谱特征的幻觉检测算法，以识别生成内容中的幻觉。通过有效地结合推理过程建模和频域特征提取，HSAD方法克服了现有方法在知识覆盖和推理偏差检测方面的局限性，表现出更高的检测准确性和鲁棒性。

## 🔬 方法详解

**问题定义**：大型语言模型在生成内容时经常出现幻觉，这严重限制了其在关键应用场景中的应用。现有的幻觉检测方法，如基于事实一致性验证的方法，受限于知识库的覆盖范围；而基于静态隐藏层特征的方法，则难以捕捉模型推理过程中的偏差，导致检测效果不佳。

**核心思路**：HSAD的核心思路是将LLM的推理过程类比于人类的认知过程，认为幻觉的产生会在LLM的隐藏层信号中留下可识别的异常模式。通过分析这些隐藏层信号，可以有效地检测出幻觉。借鉴认知神经科学中的信号分析方法，将时域信号转换到频域进行分析，能够更好地捕捉到这些异常模式。

**技术框架**：HSAD方法主要包含以下几个阶段：1. 隐藏层信号提取：从LLM的隐藏层中提取时域信号。2. 频域转换：使用快速傅里叶变换（FFT）将时域信号转换到频域，得到频谱特征。3. 特征分析：分析频谱特征，识别与幻觉相关的异常模式。4. 幻觉检测：基于频谱特征，设计幻觉检测算法，判断生成内容是否存在幻觉。

**关键创新**：HSAD的关键创新在于将频域分析引入到LLM幻觉检测中。与传统的基于静态特征的方法不同，HSAD能够捕捉到推理过程中的动态变化，从而更有效地检测出幻觉。此外，HSAD不依赖于外部知识库，因此不受知识覆盖范围的限制。

**关键设计**：HSAD的关键设计包括：1. 隐藏层选择：选择合适的隐藏层提取信号，以保证信号能够反映推理过程的关键信息。2. 频谱特征提取：设计合适的频谱特征，以捕捉与幻觉相关的异常模式。例如，可以提取频谱的能量、频率分布等特征。3. 幻觉检测算法：设计有效的幻觉检测算法，例如可以使用机器学习分类器，基于频谱特征对生成内容进行分类，判断是否存在幻觉。

## 📊 实验亮点

论文通过实验验证了HSAD的有效性，结果表明，HSAD在幻觉检测任务中取得了比现有方法更高的准确率和鲁棒性。具体性能数据（例如，准确率提升百分比）在原文中未明确给出，但摘要强调了其优于现有方法的性能表现。HSAD的优势在于其不依赖外部知识库，且能有效捕捉推理过程中的偏差。

## 🎯 应用场景

HSAD可应用于各种需要高可靠性的LLM应用场景，如金融分析、医疗诊断、法律咨询等。通过提高LLM生成内容的准确性和可靠性，HSAD有助于提升用户信任度，并降低因幻觉导致的风险。未来，该方法可进一步扩展到其他类型的生成模型，并与其他幻觉缓解技术相结合，构建更安全可靠的AI系统。

## 📄 摘要（原文）

> Although Large Language Models have demonstrated powerful capabilities in a wide range of tasks such as language understanding and code generation, the frequent occurrence of hallucinations during the generation process has become a significant impediment to their deployment in critical application scenarios. Current mainstream hallucination detection methods rely on factual consistency verification or static hidden layer features. The former is constrained by the scope of knowledge coverage, while the latter struggles to capture reasoning biases during the inference process. To address these issues, and inspired by signal analysis methods in cognitive neuroscience, this paper proposes a hallucination detection method based on the frequency-domain analysis of hidden layer temporal signals, named HSAD (\textbf{H}idden \textbf{S}ignal \textbf{A}nalysis-based \textbf{D}etection). First, by treating the LLM's reasoning process as a cognitive journey that unfolds over time, we propose modeling and simulating the human process of signal perception and discrimination in a deception-detection scenario through hidden layer temporal signals. Next, The Fast Fourier Transform is applied to map these temporal signals into the frequency domain to construct spectral features, which are used to capture anomalies that arise during the reasoning process; analysis experiments on these spectral features have proven the effectiveness of this approach. Finally, a hallucination detection algorithm is designed based on these spectral features to identify hallucinations in the generated content. By effectively combining the modeling of the reasoning process with frequency-domain feature extraction, the HSAD method overcomes the limitations of existing approaches in terms of knowledge coverage and the detection of reasoning biases, demonstrating higher detection accuracy and robustness.

