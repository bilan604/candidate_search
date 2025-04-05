from typing import Optional, Union
from maimai_helper import MaiMaiHelper


class Arguments(object):
    def __init__(self, platform: Optional[str], title: Optional[str], project_name: str, job_description: str, cutoff_pct: int, instructions: str):
        self.platform = platform
        self.title = title
        self.project_name = project_name
        self.job_description = job_description
        self.cutoff_pct = cutoff_pct
        self.instructions = instructions


if __name__ == "__main__":

    arguments = Arguments(
        platform= "Maimai",
        project_name="Entitlement Lead",
        title= "Entitlement Lead",
        job_description="""
    Job Responsibilities:
    ● Lead the planning, design, and implementation of DP’s entitlement products at platform; build mature product design methodologies to establish a lifecycle management mechanism for entitlement products.
    ● Commercial product design: Design flexible and forward-looking commercial models and structures based on the characteristics of various regions and industries around the world.
    ● Systematic product design: collect, abstract and analyze requirements from internal and external resources, document product system requirements, and follow-up the implementations.
    ● Product application: be accountable for product promotion and application to clients, and the design of integration solutions to meet client needs; collect data and feedback to continuously iterate and optimize the products.
    ● Product lifecycle management: deeply understand the business model and ecosystem of entitlement products, and establish lifecycle management mechanisms including product planning, promotion, and implementation.

    Job Requirements:
    ● Bachelor's degree or higher, with at least 5 years of end-to-end experience in product design and implementation with ToB product design mindset.
    ● Strong English proficiency is a MUST, capable of using English as a working language.
    ● Experience in product planning and implementation from scratch; excellent communication and collaboration skills, cross-team cooperation ability, and stress resistance; strong product sensitivity, model design, and operational capabilities.
    ● Be able to overall manage end-to-end entitlement product launch, from planning to implementation, based on business requirements and company strategy. Be capable of combining existing platform capabilities to develop products, and guiding internal and external team members to achieve business goals.
    ● Proven experience in designing product commercial models and strategies.
    """,
        cutoff_pct=70,
        instructions="""
    I’m from a headhunting company working on Executive Search for the company DragonPass.

    Here is a PDF containing a job description. Remember the contents of the PDF. We have a bunch of candidates we need to contact, and need to know which the priority in which to contact them with - determined by the relevance of their background and how strong the candidate is. I will be providing you copy-pasted candidate profiles. Your task is to give a percentage score for how strong the candidate is, for the given candidate in the Candidate Information section below.

    For each candidate I send you, respond by first indicating a percentage score (from 0% - 100%), followed by a brief explanation (under 150 words) as to why.

    """
    )

    mmh = MaiMaiHelper(18121303618, arguments)
    mmh.start()






