---
layout: default
title: Med-VCD: Mitigating Hallucination for Medical Large Vision Language Models through Visual Contrastive Decoding
---

# Med-VCD: Mitigating Hallucination for Medical Large Vision Language Models through Visual Contrastive Decoding

**arXiv**: [2512.01922v1](https://arxiv.org/abs/2512.01922) | [PDF](https://arxiv.org/pdf/2512.01922.pdf)

**作者**: Zahra Mahdavi, Zahra Khodakaramimaghsoud, Hooman Khaloo, Sina Bakhshandeh Taleshani, Erfan Hashemi, Javad Mirzapour Kaleybar, Omid Nejati Manzari

---

## 💡 一句话要点

**提出Med-VCD方法，通过视觉对比解码缓解医疗大视觉语言模型的幻觉问题**

**关键词**: `医疗大视觉语言模型` `幻觉缓解` `视觉对比解码` `稀疏令牌选择` `医疗视觉问答` `医疗报告生成`

## 📋 核心要点

1. 医疗大视觉语言模型在医疗应用中易产生看似合理但错误的幻觉输出
2. Med-VCD采用稀疏视觉对比解码，动态选择视觉信息令牌，无需二次解码，平衡效率与可靠性
3. 在八个医疗数据集上评估，平均提升事实准确性13%，幻觉准确性6%

## 📄 摘要（原文）

> Large vision-language models (LVLMs) are now central to healthcare applications such as medical visual question answering and imaging report generation. Yet, these models remain vulnerable to hallucination outputs that appear plausible but are in fact incorrect. In the natural image domain, several decoding strategies have been proposed to mitigate hallucinations by reinforcing visual evidence, but most rely on secondary decoding or rollback procedures that substantially slow inference. Moreover, existing solutions are often domain-specific and may introduce misalignment between modalities or between generated and ground-truth content. We introduce Med-VCD, a sparse visual-contrastive decoding method that mitigates hallucinations in medical LVLMs without the time overhead of secondary decoding. Med-VCD incorporates a novel token-sparsification strategy that selects visually informed tokens on the fly, trimming redundancy while retaining critical visual context and thus balancing efficiency with reliability. Evaluations on eight medical datasets, spanning ophthalmology, radiology, and pathology tasks in visual question answering, report generation, and dedicated hallucination benchmarks, show that Med-VCD raises factual accuracy by an average of 13\% and improves hallucination accuracy by 6\% relative to baseline medical LVLMs.

